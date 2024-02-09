<script>
	import Label from '$lib/components/ui/label/label.svelte';
	import Input from '$lib/components/ui/input/input.svelte';
	import Button from '$lib/components/ui/button/button.svelte';
</script>

<div class="flex min-h-screen flex-col items-center justify-center py-6">
	<div class="w-full max-w-sm space-y-4">
		<div class="space-y-2 text-center">
			<h1 class="text-3xl font-bold">Login</h1>
			<p class="text-gray-500 dark:text-gray-400">
				Enter your email below to login to your account
			</p>
		</div>
		<div class="space-y-4">
			<div class="space-y-2">
				<Label>Email</Label>
				<Input id="email" placeholder="m@example.com" required type="email" />
			</div>
			<div class="space-y-2">
				<div class="flex items-center">
					<Label>Password</Label>
					<a class="ml-auto inline-block text-sm underline" href="#"> Forgot your password? </a>
				</div>
				<Input id="password" required type="password" />
			</div>
			<Button class="w-full">Login</Button>
			<a class=" underline" href="/register">
				<Button class="w-full mt-4" variant="outline">Don't have an account? Sign up</Button>
			</a>
		</div>
	</div>
</div>
