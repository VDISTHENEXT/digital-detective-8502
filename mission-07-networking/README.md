# Mission 7 — How computers communicate

## 1. Task / objective
Explore fundamental computer networking principles:
- Define and provide real-world examples for core networking concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, Client-server).
- Conduct reachability and DNS lookup experiments using macOS Terminal tools (`ping` and `nslookup`) with a public domain (`example.com`).
- Trace and explain the 6-step lifecycle of what happens when a web browser loads a website.

## 2. Work completed

### Task 7.1 — Networking Concepts Reference

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A network connecting computers and devices across a small, confined geographical area such as a single room, home, or office building. | A home Wi-Fi network connecting a laptop, smartphone, and wireless printer. |
| **MAN (Metropolitan Area Network)** | A high-speed network that spans a larger geographical area than a LAN, such as an entire university campus or municipal city district. | A university campus network connecting libraries, academic departments, and dormitories across campus. |
| **WAN (Wide Area Network)** | A large-scale telecommunications network that spans vast geographical distances, connecting cities, states, or continents. | The global Internet, or an international banking network connecting ATM machines worldwide. |
| **DNS (Domain Name System)** | A decentralized directory service that converts human-friendly domain names into machine-routable IP addresses. | Translating `example.com` into IP address `172.66.147.243`. |
| **Router** | A network hardware device that reads packet destination IP addresses and forwards them between different networks along the optimal path. | A home Wi-Fi gateway router that routes data packets between local devices and the Internet Service Provider (ISP). |
| **Protocol** | A standardized set of rules and syntax formatting that governs how network devices transmit, verify, and acknowledge data. | HTTP/HTTPS for web document transfer, TCP for reliable packet delivery, and IP for addressing. |
| **Packet switching** | A transmission method where data is segmented into small, individually addressed chunks (packets) that travel along dynamic routes and reassemble at the target. | Streaming a video where thousands of distinct data packets travel across different Internet routers and recombine seamlessly on the screen. |
| **Client-server** | An architecture where client devices initiate service or data requests, and centralized server machines process and return the requested resources. | A web browser (client) requesting a web page from a remote web server (server). |

---

### Task 7.2 — Practical Network Observations

Executed reachability and lookup tests on public test domain `example.com`:

#### 1. Reachability Test (`ping -c 3 example.com`)
```text
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=58 time=28.533 ms
64 bytes from 172.66.147.243: icmp_seq=1 ttl=58 time=35.575 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=58 time=16.005 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 16.005/26.704/35.575/8.093 ms
```
- **What a connectivity test shows:** `ping` sends ICMP Echo Request packets to verify whether a remote host is online, reachable, and responsive. It measures round-trip latency (average 26.7 ms) and packet loss (0.0%).
- **What it cannot establish:** `ping` only tests basic network-layer reachability. It cannot confirm whether the web server application (HTTP/HTTPS service) is functioning properly or if the website content is error-free.

#### 2. DNS Lookup Test (`nslookup example.com`)
```text
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Address: 104.20.23.154
```
- **What a DNS lookup displays:** Shows the DNS resolver used (Google Public DNS `8.8.8.8` on port 53) and maps the domain `example.com` to its configured IPv4 addresses (`172.66.147.243` and `104.20.23.154`).
- **Role of DNS in web browsing:** When a user types a website name into a browser, humans remember words, but network routers only route packets using numerical IP addresses. DNS acts as the phonebook of the Internet, resolving domain names into IP addresses in milliseconds.

---

### Task 7.3 — Step-by-Step: What Happens When You Open a Website?

1. **User Request (Client):** The user types `https://example.com` into the address bar of a web browser running on their computer (the **client**).
2. **DNS Resolution:** The client checks its local cache; if not found, it queries a **DNS** resolver server to look up the domain name `example.com`. The DNS returns the destination IP address (`172.66.147.243`).
3. **Establishing Connection (Protocol):** The client initiates a TCP three-way handshake with the server at the resolved IP address, followed by a TLS handshake to negotiate cryptographic keys under the HTTPS **protocol**.
4. **Packet Routing through Network:** The browser sends an HTTP `GET` request. The data is sliced into packets, sent to the local **router**, and directed across intermediate network routers using **packet switching** to reach the destination machine.
5. **Server Processing:** The destination web **server** receives the request packets, reassembles them, parses the HTTP request, and retrieves the requested HTML document, styles, and images.
6. **Response and Rendering:** The server transmits the response back through the network as packets. Upon receipt, the client browser reassembles the packets, parses the HTML/CSS code, executes client-side scripts, and visually renders the web page on the screen.

## 3. Commands / tools used
- `ping -c 3 example.com`: Tested ICMP packet transmission, latency, and packet loss.
- `nslookup example.com`: Queried DNS servers to inspect domain-to-IP resolution.
- Text editor: Documented network architecture, concepts, and flow diagrams.

## 4. My understanding
Computer networks operate through hierarchical abstraction layers. Users interact with human-readable names and graphical browsers at the application layer, while DNS translates these names into numerical IP addresses. Underneath, transport protocols (TCP) ensure reliable delivery while Internet Protocol (IP) routers forward packets independently across the global web using packet switching. This distributed architecture ensures resilience—if one router goes down, packets automatically route through alternative paths.

## 5. Difficulties faced
- Distinguishing between network connectivity (tested by `ping`) and web application availability (HTTP response).
- Understanding how data packets find their way back to the client computer across the Internet.

## 6. How I resolved them
- Noted that `ping` uses low-level ICMP packets at the network layer, while web pages require transport-layer TCP and application-layer HTTP/HTTPS handshakes.
- Learned that each packet carries both destination and source IP addresses in its header, allowing every intermediate router to direct the server's reply back to the originating client.

## 7. Evidence / files
- `mission-07-networking/README.md`

## 8. Commit details
- Commit message: `Explain networking concepts and website communication`
- Branch: `main`
- Status: Staged, committed, and pushed to GitHub.
