<script lang="ts">
	import { onMount } from 'svelte';
	import { api, type AiDemoStatus } from '$lib/api';
	import TextAnalyzer from '$lib/components/TextAnalyzer.svelte';
	import CodeGenerator from '$lib/components/CodeGenerator.svelte';

	let aiStatus: AiDemoStatus | null = $state(null);
	let loading = $state(true);

	onMount(async () => {
		const response = await api.getAiDemoStatus();
		if (response.data) {
			aiStatus = response.data;
		}
		loading = false;
	});
</script>

<div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
	<div class="container mx-auto px-6 py-12">
		<!-- Hero Section -->
		<div class="text-center mb-16">
			<div class="inline-flex items-center gap-2 bg-blue-100 text-blue-800 px-4 py-2 rounded-full text-sm font-medium mb-6">
				<svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
					<path fill-rule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clip-rule="evenodd"></path>
				</svg>
				AI-Powered Development
			</div>
			<h1 class="text-5xl font-bold text-gray-900 mb-6">
				Expert <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">AI & Software</span> Development
			</h1>
			<p class="text-xl text-gray-600 max-w-3xl mx-auto mb-8">
				Professional freelance developer specializing in AI integration, full-stack development, and cutting-edge solutions.
				Experience the power of modern AI technology in action.
			</p>
			
			{#if loading}
				<div class="flex justify-center items-center gap-2 text-gray-500">
					<div class="animate-spin rounded-full h-5 w-5 border-b-2 border-gray-400"></div>
					<span>Checking AI services...</span>
				</div>
			{:else if aiStatus}
				<div class="flex justify-center">
					{#if aiStatus.status === 'available'}
						<div class="flex items-center gap-2 bg-green-100 text-green-800 px-4 py-2 rounded-full">
							<div class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
							<span class="font-medium">{aiStatus.message}</span>
							{#if aiStatus.model}
								<span class="text-sm opacity-75">({aiStatus.model})</span>
							{/if}
						</div>
					{:else}
						<div class="flex items-center gap-2 bg-yellow-100 text-yellow-800 px-4 py-2 rounded-full">
							<div class="w-2 h-2 bg-yellow-500 rounded-full"></div>
							<span class="font-medium">Demo mode - {aiStatus.message}</span>
						</div>
					{/if}
				</div>
			{/if}
		</div>

		<!-- Skills Overview -->
		<div class="grid md:grid-cols-3 gap-6 mb-16">
			<div class="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">AI Integration</h3>
				<p class="text-gray-600">OpenAI, Claude, custom ML models, and intelligent automation solutions.</p>
			</div>

			<div class="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Full-Stack Development</h3>
				<p class="text-gray-600">SvelteKit, React, FastAPI, Node.js, and modern web technologies.</p>
			</div>

			<div class="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
				<h3 class="text-lg font-semibold text-gray-900 mb-2">Performance & Scale</h3>
				<p class="text-gray-600">Optimized solutions, cloud deployment, and enterprise-grade architecture.</p>
			</div>
		</div>

		<!-- AI Demonstration Section -->
		<div class="mb-16">
			<div class="text-center mb-12">
				<h2 class="text-3xl font-bold text-gray-900 mb-4">AI Capabilities Demonstration</h2>
				<p class="text-lg text-gray-600 max-w-2xl mx-auto">
					Experience live AI-powered features built with modern APIs and intelligent processing.
				</p>
			</div>

			<div class="grid lg:grid-cols-2 gap-8">
				<TextAnalyzer />
				<CodeGenerator />
			</div>
		</div>

		<!-- Contact Section -->
		<div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
			<div class="text-center">
				<h2 class="text-2xl font-bold text-gray-900 mb-4">Ready to Build Something Amazing?</h2>
				<p class="text-gray-600 mb-6">
					Let's discuss your project and how AI can transform your business processes.
				</p>
				<div class="flex flex-col sm:flex-row gap-4 justify-center">
					<a href="mailto:contact@example.com" class="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors font-medium">
						Start a Project
					</a>
					<a href="#portfolio" class="bg-gray-100 text-gray-800 px-6 py-3 rounded-lg hover:bg-gray-200 transition-colors font-medium">
						View Portfolio
					</a>
				</div>
			</div>
		</div>
	</div>
</div>
