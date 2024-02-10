<script lang="ts">
    import Label from "$lib/components/ui/label/label.svelte";
    import Input from "$lib/components/ui/input/input.svelte";
    import Button from "$lib/components/ui/button/button.svelte";

</script>

<div class="mx-auto max-w-6xl px-4 flex flex-col gap-4">
    <header class="flex items-center py-6 space-x-4">
      <a class="flex items-center space-x-2" href="#">
        <img
          alt="Logo"
          class="rounded-full"
          height="40"
          src="/placeholder.svg"
          width="40"
        />
        <span class="font-bold text-xl">Election Commission</span>
      </a>
      <nav class="ml-auto flex items-center space-x-4">
        <a class="font-medium underline" href="#">
          Election Information
        </a>
      </nav>
    </header>
    <main class="grid gap-8">
      <div class="space-y-2">
        <h1 class="text-4xl font-extrabold tracking-tight">Voter Registration</h1>
        <p class="text-gray-500 dark:text-gray-400">Enter your information to register to vote</p>
      </div>
      <a class=" underline" href="/login">
				<Button class="w-full mt-4" variant="outline">Already registered? Sign in to vote</Button>
			</a>
      <div class="grid gap-4">
        <div class="grid grid-cols-2 gap-4 sm:grid-cols-1">
          <div class="space-y-2">
            <Label>Full Name</Label>
            <Input id="name" placeholder="John Doe" required />
          </div>
          <div class="space-y-2">
            <Label>Address</Label>
            <Input id="address" placeholder="123 Main St" required />
          </div>
        </div>
        <div class="grid grid-cols-2 gap-4">
          <div class="space-y-2">
            <Label>Date of Birth</Label>
            <Input id="dob" required type="date" />
          </div>
          <div class="space-y-2">
            <Label>Voter ID</Label>
            <Input id="voter-id" placeholder="V123456" required />
          </div>
        </div>
        <Button class="w-full">Submit Registration</Button>
      </div>
    </main>
  </div>