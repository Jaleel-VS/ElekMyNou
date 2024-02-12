<script lang="ts">
    import CardContent from "$lib/components/ui/card/card-content.svelte";
    import Card from "$lib/components/ui/card/card.svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    import logo from "$lib/assets/logo.png";
    import hero from "$lib/assets/hero.jpg";

    
</script>

<div class="flex flex-col min-h-[100dvh]">
    <header class="px-4 lg:px-6 h-auto flex items-center">
      <div class="flex items-center space-x-2">
        <img
          alt="Logo"
          class="h-[5.5rem] w-auto p-2"
          height="40"
          src={logo}
          width="40"
        />
        <h1 class="text-xl font-bold tracking-tighter sm:text-2xl xl:text-3xl">National Elections</h1>
      </div>
      <nav class="ml-auto flex flex-col items-center p-2 gap-3 sm:flex-row sm:items-center sm:gap-6 lg:gap-8">
        <a class="text-sm font-medium hover:underline underline-offset-4" href="/candidates">
          Candidates
        </a>
        <a class="text-sm font-medium hover:underline underline-offset-4" href="/results">
          Results
        </a>
      </nav>
    </header>
    <main class="flex-1">
      <section class="w-full py-6 md:py-12 lg:py-16 xl:py-20 bg-gray-100 dark:bg-gray-800">
        <div class="container flex flex-col items-center justify-center gap-4 px-4 md:px-6 text-center">
          <div class="space-y-2">
            <h1 class="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">Your Vote. Your Voice.</h1>
            <p class="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
              The National Elections 2024. Make your vote count. Let your voice be heard.
            </p>
          </div>
          <a
            class="inline-flex h-10 items-center justify-center rounded-md border border-gray-200 bg-white px-4 text-sm font-medium shadow-sm transition-colors hover:bg-gray-100 hover:text-gray-900 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-gray-950 disabled:pointer-events-none disabled:opacity-50 dark:border-gray-800 dark:bg-gray-950 dark:hover:bg-gray-800 dark:hover:text-gray-50 dark:focus-visible:ring-gray-300"
            href="/login"
          >
            Vote Now
          </a>
        </div>
      </section>
      <section class="w-full py-6 md:py-12 lg:py-16">
        <div class="container grid items-center gap-4 px-4 md:px-6 lg:grid-cols-[1fr_600px] lg:gap-10">
          <img
            alt="Hero"
            class="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full lg:order-last"
            height="320"
            src={hero}
            width="600"
          />
          <div class="flex flex-col justify-center space-y-4">
            <div class="space-y-2">
              <h2 class="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">About the Elections</h2>
              <p class="max-w-[600px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed dark:text-gray-400">
                The National Elections are held every four years. It is a time for the citizens to choose their
                leaders who will represent them in the government. The elections are a symbol of democracy and give
                the people the power to make their voices heard.
              </p>
            </div>
          </div>
        </div>
      </section>
    </main>
    <footer class="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t">
      <p class="text-xs text-gray-500 dark:text-gray-400">Share the Elections with your friends</p>
      <div class="space-x-4 sm:ml-auto flex items-center gap-4 sm:gap-6">
        <Button variant="outline">
            <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                <path fill-rule="evenodd" d="M13.1 6H15V3h-1.9A4.1 4.1 0 0 0 9 7.1V9H7v3h2v10h3V12h2l.6-3H12V6.6a.6.6 0 0 1 .6-.6h.5Z" clip-rule="evenodd"/>
              </svg>            
          Share on Facebook
        </Button>
        <Button variant="outline">
            <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                <path fill-rule="evenodd" d="M22 5.9c-.7.3-1.5.5-2.4.6a4 4 0 0 0 1.8-2.2c-.8.5-1.6.8-2.6 1a4.1 4.1 0 0 0-6.7 1.2 4 4 0 0 0-.2 2.5 11.7 11.7 0 0 1-8.5-4.3 4 4 0 0 0 1.3 5.4c-.7 0-1.3-.2-1.9-.5a4 4 0 0 0 3.3 4 4.2 4.2 0 0 1-1.9.1 4.1 4.1 0 0 0 3.9 2.8c-1.8 1.3-4 2-6.1 1.7a11.7 11.7 0 0 0 10.7 1A11.5 11.5 0 0 0 20 8.5V8a10 10 0 0 0 2-2.1Z" clip-rule="evenodd"/>
              </svg>  
              
          Share on Twitter
        </Button>
        
      </div>
    </footer>
  </div>