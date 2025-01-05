<!-- Matrix-style canvas background -->
<canvas id="matrix" style="position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1;"></canvas>
<script src="https://cdn.jsdelivr.net/npm/matrix-effect@1.0.1/matrix.min.js"></script>

<!-- Glitch effect CSS -->
<style>
.glitch {
  animation: glitch 1s linear infinite;
  text-shadow: 2px 0 blue, -2px 0 red;
  font-family: 'Courier New', monospace;
}
@keyframes glitch {
  2%, 64% { transform: translate(2px,0) skew(0deg); }
  4%, 60% { transform: translate(-2px,0) skew(0deg); }
  62% { transform: translate(0,0) skew(5deg); }
}

.neon-text {
  color: #fff;
  text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px #0073e6, 0 0 20px #0073e6;
  animation: neon 1.5s ease-in-out infinite alternate;
}

.terminal-window {
  background: rgba(0,0,0,0.9);
  border: 2px solid #00ff00;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 0 20px rgba(0,255,0,0.5);
  margin: 20px 0;
}

.scanline {
  width: 100%;
  height: 100px;
  background: linear-gradient(
    0deg,
    rgba(0, 255, 0, 0) 0%,
    rgba(0, 255, 0, 0.1) 10%,
    rgba(0, 255, 0, 0) 100%
  );
  position: fixed;
  top: 0;
  animation: scanline 6s linear infinite;
}

@keyframes scanline {
  0% { top: -100px; }
  100% { top: 100vh; }
}
</style>

<!-- Scanline effect -->
<div class="scanline"></div>

<!-- Retro terminal wrapper -->
<div class="terminal-window">

<!-- Cyberpunk Header -->
<div style="text-align: center; margin-bottom: 30px;">
<pre style="color: #0ff; text-shadow: 0 0 10px #0ff;">
 _____  __ __ _____ _____ _____ _____ _____ _____ 
|     ||  |  ||  _  ||   __| __  ||   __||   __| 
|   --||_   _||     ||   __| __ -||__   ||   __| 
|_____| |_|  |__|__||_____|_____||_____||_____| 
</pre>
</div>

<!-- Animated Binary Background GIF -->
<div style="position: relative;">
<img src="https://media.giphy.com/media/ko7twHhomhk8E/giphy.gif" style="width: 100%; height: 200px; object-fit: cover; border-radius: 10px; margin: 20px 0;">
<div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
<h1 class="glitch" style="color: #fff; font-size: 3em;">ROHAN PRAKASH PAWAR</h1>
</div>
</div>

<div align="center">

### <span class="neon-text">🔒 CYBER SECURITY RESEARCHER · 🤖 AI ENTHUSIAST</span>

<!-- System Status Display -->
<div style="background: #000; color: #0f0; padding: 15px; border-radius: 5px; font-family: monospace; margin: 20px 0;">
[SYSTEM STATUS: ONLINE]<br>
[LOCATION: MUMBAI, INDIA]<br>
[MISSION: ACTIVE]<br>
<div class="loading-bar" style="margin: 10px 0;">
Loading security protocols... ████████████ 100%
</div>
</div>

<!-- Social Links with Neon Effect -->
<div style="margin: 20px 0;">
<a href="mailto:r04nx@outlook.com" style="margin: 0 10px;"><img src="https://img.shields.io/badge/-r04nx@outlook.com-D14836?style=for-the-badge&logo=gmail&logoColor=white&color=000000" alt="Email"></a>
<a href="https://r04nx.tech" style="margin: 0 10px;"><img src="https://img.shields.io/badge/-r04nx.tech-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white&color=000000" alt="Website"></a>
<a href="https://github.com/r04nx" style="margin: 0 10px;"><img src="https://img.shields.io/badge/-r04nx-181717?style=for-the-badge&logo=github&logoColor=white&color=000000" alt="GitHub"></a>
</div>

<!-- Animated Terminal Text -->
<div class="terminal-text" style="background: #000; padding: 20px; border-radius: 5px; margin: 20px 0;">
<span id="typed"></span>
<script>
new Typed('#typed', {
  strings: [
    'Initializing security protocols...',
    'Running vulnerability scans...',
    'Deploying AI defenses...',
    'System secured.'
  ],
  typeSpeed: 50,
  backSpeed: 30,
  loop: true
});
</script>
</div>

<!-- Stats with Cyberpunk Theme -->
<div style="filter: drop-shadow(0 0 10px #0ff);">
<img src="https://github-readme-stats.vercel.app/api?username=r04nx&show_icons=true&theme=radical" alt="GitHub Stats">
</div>

<!-- Experience Section with Terminal Style -->
<div class="terminal-window" style="text-align: left;">
<pre style="color: #0f0;">
root@r04nx:~# cat experience.log

<span style="color: #0ff;">[CURRENT_ROLE]</span>
└─ Server & Security Administrator @ Alesa.ai
   ├─ Infrastructure Management
   ├─ Security Implementation
   └─ AI/ML Operations

<span style="color: #0ff;">[PREVIOUS_ROLES]</span>
└─ System Operations @ SPIT
└─ MLOps Engineer @ Quotientica
</pre>
</div>

<!-- Projects Section -->
<div class="terminal-window">
<pre style="color: #0f0;">
root@r04nx:~# ls -la /projects/

<span style="color: #0ff;">[ACTIVE_PROJECTS]</span>
└─📡 LoRAid SOS Connect
   ├─ Range: 10km+
   └─ Status: Operational

└─🌐 Netflask
   ├─ Network Diagnostics
   └─ Status: Deployed
</pre>
</div>

<!-- Tech Stack with Neon Icons -->
<div style="margin: 20px 0;">
<img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white&color=000000" alt="Python">
<img src="https://img.shields.io/badge/-Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white&color=000000" alt="Kali">
<img src="https://img.shields.io/badge/-AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white&color=000000" alt="AWS">
</div>

<!-- Visitor Counter with Cyberpunk Style -->
<div style="margin: 20px 0; background: #000; padding: 10px; border-radius: 5px;">
<img src="https://profile-counter.glitch.me/r04nx/count.svg" alt="Visitor Count">
</div>

<!-- Matrix Footer -->
<div style="height: 100px; overflow: hidden; margin-top: 20px;">
<canvas id="matrix-footer"></canvas>
</div>

</div>
</div>

<!-- Initialize Matrix Effect -->
<script>
// Matrix rain effect initialization code here
</script>

### 🎓 Education
- **B.Tech in Electronics & Telecommunication** (2023 - Present)  
  Sardar Patel Institute of Technology, Mumbai
- **Diploma in Computer Engineering** (2020 - 2023)  
  Government Polytechnic Hingoli | 84.80%

### 💼 Experience
<details>
<summary>🌟 Server and Security Administrator @ Alesa.ai (Nov 2024 - Present)</summary>

- Led NoULEZ project infrastructure management
- Optimized geospatial data with OSM server
- Enhanced security & deployed LLM environments
- Streamlined deployments with Docker
- Managed remote team collaboration
- Maintained AI/ML infrastructure
</details>

<details>
<summary>🔧 System and Network Operations Intern @ SPIT (July 2024 - Present)</summary>

- Deployed Cisco Meraki network devices
- Implemented on-premises VPC server solution
- Managed network security & troubleshooting
</details>

<details>
<summary>💻 Backend and MLOps Engineer @ Quotientica (Nov 2023 - Mar 2024)</summary>

- Developed ML models for fraud detection
- Optimized APIs for reduced latency
- Implemented AWS serverless architecture
</details>

### 🚀 Projects

<details>
<summary>🆘 LoRAid SOS Connect | Disaster Communication System</summary>

- Achieved 10km+ low-power wireless communication
- Implemented MQTT-based cloud DMS
- Programmed NodeMCU microcontrollers
- Status: Active Development
</details>

<details>
<summary>🌐 Netflask | Network Utility Tool</summary>

- Built Flask-based network diagnostic suite
- Features: DNS lookup, traceroute, port scanning
- Focused on security and performance
</details>

### 🛠️ Tech Stack
<img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/-AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white" alt="AWS">
<img src="https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
<img src="https://img.shields.io/badge/-Kali_Linux-557C94?style=flat-square&logo=kali-linux&logoColor=white" alt="Kali Linux">
<img src="https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react&logoColor=black" alt="React">
<img src="https://img.shields.io/badge/-Node.js-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js">
<img src="https://img.shields.io/badge/-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB">
<img src="https://img.shields.io/badge/-Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git">

### 🏆 Certifications
- EC-Council Ethical Hacking Essentials (EHE)
- Kaggle Machine Learning & Python
- TCS iON Career Edge - Young Professional
- Infosys Penetration Testing

<div style="background-color: #0d1117; padding: 10px; border-radius: 6px; margin: 10px 0;">
<pre style="color: #00ff00;">
root@r04nx:~# cat /etc/motd
Welcome to my digital fortress! 
Exploring the intersection of Cybersecurity and AI
</pre>
</div>

<div align="center">
<img src="https://github-readme-streak-stats.herokuapp.com/?user=r04nx&theme=radical" alt="GitHub Streak">
</div>

### <span style="color: #00ff00;">🛠️ ARSENAL</span>

<div style="background: #000; padding: 15px; border-radius: 5px; border: 1px solid #00ff00;">
<img src="https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/-Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white" alt="Kali Linux">
</div>

<!-- ASCII art terminal -->
<div style="background: #000; padding: 20px; border-radius: 5px; margin: 20px 0;">
<pre style="color: #00ff00;">
root@r04nx:~# whoami
┌──(r04nx㉿kali)-[~/projects]
└─$ cat /etc/motd
Welcome to my digital fortress! 
Exploring the intersection of Cybersecurity and AI
</pre>
</div>

<!-- Animated visitor counter -->
<div style="margin: 20px 0;">
<img src="https://profile-counter.glitch.me/r04nx/count.svg" alt="Visitor Count">
</div>

<!-- Matrix rain effect at the bottom -->
<div style="height: 100px; overflow: hidden; margin-top: 20px;">
<canvas id="matrix-footer"></canvas>
</div>

<!-- Interactive Hacker Quote Generator -->
<div class="terminal-window">
<pre style="color: #0f0;" id="hacker-quote">
root@r04nx:~# fortune | cowsay
 _________________________________________
/ "First, solve the problem. Then, write   \
\ the code." - John Johnson                /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
</pre>
<button onclick="newQuote()" style="background: #0f0; color: #000; border: none; padding: 10px; border-radius: 5px; margin: 10px 0;">Generate Quote</button>
</div>

<!-- Interactive Skills Tree -->
<div class="terminal-window">
<pre style="color: #0f0;">
root@r04nx:~# cat skills_tree.txt

SKILL TREE [Level 42]
====================
🔒 Security [■■■■■■■■■□] 90%
├── Penetration Testing [■■■■■■■■□□] 80%
├── Network Security   [■■■■■■■■■□] 90%
└── Cloud Security    [■■■■■■■□□□] 70%

🤖 AI/ML [■■■■■■■■□□] 80%
├── Deep Learning     [■■■■■■■□□□] 70%
├── NLP              [■■■■■■□□□□] 60%
└── Computer Vision  [■■■■■■■□□□] 70%

💻 Development [■■■■■■■■□□] 80%
├── Backend          [■■■■■■■■■□] 90%
├── DevOps           [■■■■■■■□□□] 70%
└── System Design    [■■■■■■■■□□] 80%
</pre>
</div>

<!-- Hacker Meme Collection -->
<div class="terminal-window">
<h3 style="color: #0f0;">root@r04nx:~# ls /memes/</h3>
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 20px 0;">
<img src="https://media.giphy.com/media/115BJle6N2Av0A/giphy.gif" alt="Hacking in Progress" style="width: 100%; border-radius: 5px;">
<img src="https://media.giphy.com/media/ZY3W96Mvat8EFTCclA/giphy.gif" alt="Matrix Code" style="width: 100%; border-radius: 5px;">
<img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" alt="Bug Finding" style="width: 100%; border-radius: 5px;">
<img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" alt="Cyber Security" style="width: 100%; border-radius: 5px;">
</div>
</div>

<!-- Interactive Terminal -->
<div class="terminal-window">
<pre style="color: #0f0;" id="terminal-output">
root@r04nx:~# Type 'help' for available commands
</pre>
<input type="text" id="terminal-input" 
       style="background: #000; color: #0f0; border: none; width: 100%; padding: 10px; outline: none; font-family: monospace;"
       placeholder="Enter command...">
</div>

<!-- Cyberpunk Quotes Carousel -->
<div class="terminal-window">
<div id="quote-carousel" style="color: #0ff; text-align: center; padding: 20px;">
"The only way to do great work is to love what you do." - Steve Jobs
</div>
</div>

<!-- Achievement Badges -->
<div class="terminal-window">
<h3 style="color: #0f0;">ACHIEVEMENTS UNLOCKED</h3>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin: 20px 0;">
<div style="border: 1px solid #0f0; padding: 10px; border-radius: 5px; text-align: center;">
🏆 Bug Hunter
<br>Level: Elite
</div>
<div style="border: 1px solid #0f0; padding: 10px; border-radius: 5px; text-align: center;">
🚀 Code Ninja
<br>Level: Master
</div>
<div style="border: 1px solid #0f0; padding: 10px; border-radius: 5px; text-align: center;">
🤖 AI Wizard
<br>Level: Advanced
</div>
</div>
</div>

<!-- Current Status -->
<div class="terminal-window">
<pre style="color: #0f0;">
root@r04nx:~# systemctl status r04nx
● r04nx.service - Cyber Security Researcher
     Active: active (running)
     Status: Currently working on AI Security
     CPU: 98.2%
     RAM: 16GB/32GB
     Uptime: 42 days
     Last Commit: 2 hours ago
</pre>
</div>

<!-- Fun Easter Egg -->
<div style="display: none;" id="easter-egg">
<pre style="color: #0f0;">
You found the secret! Here's a cookie 🍪
</pre>
</div>

<!-- Interactive Scripts -->
<script>
// Hacker quotes array
const hackerQuotes = [
    "Programming is not about typing, it's about thinking.",
    "There are 10 types of people in the world: those who understand binary and those who don't.",
    "It's not a bug – it's an undocumented feature.",
    "Real hackers count from 0",
    "Keep calm and git commit"
];

// Generate new quote
function newQuote() {
    const quote = hackerQuotes[Math.floor(Math.random() * hackerQuotes.length)];
    document.getElementById('hacker-quote').innerText = quote;
}

// Simple terminal commands
const terminalInput = document.getElementById('terminal-input');
const terminalOutput = document.getElementById('terminal-output');

terminalInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        const command = this.value;
        handleCommand(command);
        this.value = '';
    }
});

function handleCommand(cmd) {
    let output = '';
    switch(cmd) {
        case 'help':
            output = `Available commands:
- help: Show this help
- about: About me
- skills: Show skills
- contact: Contact info
- clear: Clear terminal`;
            break;
        case 'about':
            output = 'Cyber Security Researcher & AI Enthusiast';
            break;
        case 'clear':
            terminalOutput.innerHTML = '';
            return;
        default:
            output = `Command not found: ${cmd}`;
    }
    terminalOutput.innerHTML += `\n$ ${cmd}\n${output}`;
}

// Easter egg trigger
document.addEventListener('konami', function() {
    document.getElementById('easter-egg').style.display = 'block';
});
</script>

<!-- Retro Footer -->
<div style="text-align: center; margin-top: 40px; border-top: 1px solid #0f0; padding-top: 20px;">
<pre style="color: #0f0;">
SYSTEM SHUTDOWN SEQUENCE
[■■■■■■■■■■] 100%
Connection terminated...
</pre>
</div>
