---
title: Installing Aspose.Cells for Reporting Services
type: docs
weight: 20
url: /reportingservices/installing-aspose-cells-for-reporting-services/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Aspose.Cells for Reporting Services extends Microsoft SQL Server Reporting Services (SSRS) with powerful spreadsheet generation capabilities. This page walks you through the two supported installation methods—**MSI installer** and **DLL‑only**—and shows how to safely uninstall the product when it’s no longer needed.

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Installation Options Overview](#installation-options-overview)  
   - [Using the MSI Installer](#using-the-msi-installer)  
   - [Using DLL Only](#using-dll-only)  
3. [Uninstalling Aspose.Cells for Reporting Services](#uninstalling-asposecells-for-reporting-services)  

## Prerequisites {#prerequisites}

| Requirement | Minimum Version |
|-------------|-----------------|
| **Microsoft SQL Server** | 2005 or later |
| **.NET Framework** | 3.5 or later |
| **Operating System** | Windows Server 2005 or later |
| **Visual Studio** | 2005 or later |
| **Microsoft Excel** | 2003 or later |

## Installation Options Overview {#installation-options-overview}

Aspose.Cells for Reporting Services can be installed in two ways, each suited to different deployment scenarios:

| Method | When to Use | Key Benefits |
|--------|-------------|--------------|
| [**MSI Installer**](/cells/reportingservices/using-msi-installer/) | Standard on‑premises environments where you want a quick, wizard‑driven setup. | Automatic registration of the extension, easy rollback, and built‑in repair feature. |
| [**DLL Only**](/cells/reportingservices/using-dll-only/) | Cloud‑based or containerized deployments where you control the runtime and prefer a lightweight package. | No installer footprint, full control over versioning, and easy integration with CI/CD pipelines. |

## Using the MSI Installer {#using-the-msi-installer}

1. **Download the MSI**  
   Obtain the latest MSI package from the [Aspose.Cells for Reporting Services download page](https://releases.aspose.com/cells/reportingservices/).

2. **Run the Installer**  
   [Run the MSI installer](/cells/reportingservices/using-msi-installer/) and follow the prompts.

## Using DLL Only {#using-dll-only}

[How to install using dll only](/cells/reportingservices/using-dll-only/)

## Uninstalling Aspose.Cells for Reporting Services {#uninstalling-asposecells-for-reporting-services}

 1. Open **Control Panel → Programs and Features**.
 1. Locate **Aspose.Cells for Reporting Services**.
 1. Click **Uninstall** and follow the wizard.

> **Note:** After removal, clear the SSRS cache (`C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer\Cache`) to avoid stale references.

This section includes the following topics:

- [Using MSI Installer](/cells/reportingservices/using-msi-installer/)
- [Using DLL Only](/cells/reportingservices/using-dll-only/)
- [Uninstalling Aspose.Cells for Reporting Services](/cells/reportingservices/uninstalling-aspose-cells-for-reporting-services/)
