# network_ip_monitor

## Overview

This Odoo module, `network_ip_monitor`, provides a basic framework for managing and monitoring network IP addresses within your IT infrastructure. It allows you to track essential details such as the IP address itself, its type (IPv4 or IPv6), its current status (active, inactive, or blacklisted), and a descriptive note.

This module is designed to be lightweight and easily expandable, making it a useful tool for IT administrators and companies managing their network infrastructure. It is published under the LGPL-3.0 license, promoting open collaboration and usage.

## Features

* **Network IP Address Management:**
    * Define and store network IP addresses.
    * Categorize IP addresses by type (IPv4/IPv6).
    * Track the status of each IP address (active, inactive, blacklisted).
    * Add a description for each IP address for better context.
* **Basic Security:**
    * Implements a dedicated security group, "Network IP Manager", to control access to the module's features.
    * Defines model access rules to ensure only authorized users can create, read, write, and delete network IP records.
* **User Interface:**
    * Provides intuitive list and form views for easy management of IP address records within Odoo.
    * Includes a dedicated "Network Monitor" menu in Odoo with a submenu "IP Addresses" to access the IP management features.

## Installation

1.  Place the `network_ip_monitor` directory within your Odoo addons path.
2.  Activate developer mode in your Odoo instance.
3.  Go to the "Apps" menu and click "Update Apps List".
4.  Search for "Network IP Monitor" and click "Install".

## Configuration

After installation, a new top-level menu named "Network Monitor" will be available. Under this menu, you will find the "IP Addresses" submenu, which allows you to access the list and form views for managing network IP addresses.

## License

This module is published under the [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html) license.

## Contributing

Contributions to this module are welcome. Please feel free to fork the repository and submit pull requests with your enhancements or bug fixes.

## Further Development

This module provides a solid foundation for a more comprehensive cyber security Odoo suite. Potential future enhancements include:

* Integration with network scanning tools.
* Alerting and notifications for IP status changes.
* Tracking historical status changes of IP addresses.
* More advanced filtering and reporting capabilities.
* Additional models for managing related network information (e.g., MAC addresses, hostnames).