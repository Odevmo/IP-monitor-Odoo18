# network_ip_monitor

## Overview

This Odoo module provides core IP address tracking and basic security insights, logging user IP addresses upon login and checking them against the Tor exit node list. It serves as a foundational component for a broader cybersecurity suite planned for Odoo 18+.

## Features

* **User IP Logging:** Records user IP addresses upon successful login.
* **Tor Exit Node Detection:** Automatically checks if a logged IP address is a Tor exit node.
* **"Network Monitor" Menu:** Provides a dedicated menu for accessing IP-related features.
* **"User IPs" View:** Allows viewing and managing recorded user IP addresses, including Tor exit status.
* **Security Group:** Implements "Network IP Manager" for controlled access.

## Installation

1.  Place the `network_ip_monitor` directory in your Odoo addons path.
2.  Enable developer mode in Odoo.
3.  Update the Apps List.
4.  Install "Network IP Monitor".

## Configuration

A "Network Monitor" menu with a "User IPs" submenu will be available. Access control is managed via the "Network IP Manager" security group (Users & Companies > Users > Access Rights). Administrators have implicit access.

## License

[LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html)

## Contributing

Contributions are welcome. Fork and submit pull requests.

## Roadmap

This module is the first step towards a comprehensive cybersecurity suite for Odoo 18+, with future enhancements planned.