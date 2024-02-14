<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { tick } from 'svelte';

	export let endDate: Date;
	export let startDate: Date;

	let remainingTime = calculateRemainingTime();

	function calculateRemainingTime() {
		const now = new Date();
		if (now < startDate) {
			return { days: -1, hours: -1, minutes: -1, seconds: -1 };
		} else if (now > endDate) {
			return { days: 0, hours: 0, minutes: 0, seconds: 0 };
		} else {
			const timeDifference = endDate.getTime() - now.getTime();
			const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
			const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
			const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));
			const seconds = Math.floor((timeDifference % (1000 * 60)) / 1000);
			return { days, hours, minutes, seconds };
		}
	}

	let timerInterval: number | undefined;

	onMount(() => {
		timerInterval = setInterval(() => {
			remainingTime = calculateRemainingTime();
			tick();
		}, 1000);
	});

	onDestroy(() => {
		clearInterval(timerInterval);
	});
</script>

<h2 class="text-center text-2xl font-semibold mb-4">Time Left to Vote</h2>

<div class="flex h-full w-full items-center justify-center">
	<div class="flex flex-row items-center gap-3">
		{#if remainingTime.days >= 0}
			<div class="flex justify-center flex-col">
				<div class="text-4xl font-semibold">{remainingTime.days}</div>
				<div class="text-xs font-semibold">days</div>
			</div>
			<div class="flex justify-center flex-col">
				<div class="text-4xl font-semibold">{remainingTime.hours}</div>
				<div class="text-xs font-semibold">hours</div>
			</div>
			<div class="flex justify-center flex-col">
				<div class="text-4xl font-semibold">{remainingTime.minutes}</div>
				<div class="text-xs font-semibold">minutes</div>
			</div>
			<div class="flex justify-center flex-col">
				<div class="text-4xl font-semibold">{remainingTime.seconds}</div>
				<div class="text-xs font-semibold">seconds</div>
			</div>
		{:else if remainingTime.days === -1}
			<div class="text-lg font-semibold text-gray-500">Not started</div>
		{:else}
			<div class="text-lg font-semibold text-gray-500">0d 0h 0m 0s</div>
		{/if}
	</div>
</div>
