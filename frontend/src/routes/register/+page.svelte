<script lang="ts">
    import Label from "$lib/components/ui/label/label.svelte";
    import Input from "$lib/components/ui/input/input.svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    import logo from "$lib/assets/logo.png";

</script>

<div class="mx-auto max-w-6xl px-4 flex flex-col gap-4">
    <header class="flex items-center py-6 space-x-4">
      <a class="flex items-center space-x-2" href="/">
        <img
          alt="Logo"
          height="40"
          src={logo}
          width="40"
        />
        <span class="font-bold text-xl">Election Commission</span>
      </a>
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
        <div class="grid grid-cols-2 gap-4">
          <div class="space-y-2">
            <Label>First Name</Label>
            <Input id="first-name" placeholder="John" required />
          </div>
          <div class="space-y-2">
            <Label>Last Name</Label>
            <Input id="first-name" placeholder="Doe" required />
          </div>
          <div class="space-y-2">
            <Label>Address</Label>
            <Input id="address" placeholder="123 Main St" required />
          </div>
          <div class="space-y-2">
            <Label>SA ID number</Label>
            <Input id="voter-id" placeholder="" type="number" required />
          </div>
          <div class="space-y-2">
            <Label>Email Address</Label>
            <Input id="email-add" placeholder="abc@example.com" type="email" required />
            <Button>Verify</Button>
          </div>
          <div class="space-y-2">
            <Label>Voting Province</Label>
            <Input id="voting-prov" placeholder="abc@example.com" type="dropdown" required />
            <Button>Verify</Button>
          </div>
          <!-- verify email button -->

        </div>
        <Button class="w-full">Submit Registration</Button>
      </div>
    </main>
  </div>
