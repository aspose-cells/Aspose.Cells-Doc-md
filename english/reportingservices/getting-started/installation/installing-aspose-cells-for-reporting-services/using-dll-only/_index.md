---
title: Using DLL Only
type: docs
weight: 20
url: /reportingservices/using-dll-only/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

**Using Aspose.Cells for Reporting Services – DLL‑Only Installation**  

This guide explains how to install **Aspose.Cells for Reporting Services** when you want to work only with the DLL files (no MSI/Setup packages).  

## 📦 1. Download the Component  

1. Open the [Aspose.Cells for Reporting Services download page](https://downloads.aspose.com/cells/reportingservices).  
2. Download the **Aspose.Cells for Reporting Services (zip)** archive – it contains the latest DLLs and documentation.  

### Supported DLL packages  

| Folder (inside the ZIP) | SSRS version supported |
|--------------------------|------------------------|
| `SSRS2005`               | SQL Server 2005 Reporting Services |
| `SSRS2008`               | SQL Server 2008 Reporting Services |
| `SSRS2008R2`             | SQL Server 2008 R2 / 2012 / 2014 Reporting Services |
| `SSRS2016`               | SQL Server 2016 / 2017 / 2019 Reporting Services |
| `PBIRS`                  | Power BI Report Server |

> **Tip:** Choose the folder that matches the SSRS version you are using. The DLL inside each folder is named `Aspose.Cells.ReportingServices.dll`.

## 📁 2. Extract the Archive  

Extract the ZIP to a folder of your choice, e.g.:

```text
C:\Aspose\CellsReportingServices\
```

## 🛠️ 3. Install the Report Designer Add‑in (Excel)  

The Designer add‑in lets you design reports directly from Excel.

1. Open a **Developer Command Prompt** (run as Administrator).  
2. Register the client assembly with **RegAsm.exe**:

```powershell
"%WINDIR%\Microsoft.NET\Framework\v4.0.30319\RegAsm.exe" ^
    "C:\Aspose\CellsReportingServices\Aspose.Cells.ReportingServices.Client.dll" /codebase
```

> **Note:** Use the 64‑bit `RegAsm.exe` (`Framework64`) if your Office installation is 64‑bit.

3. Open Excel → **File → Options → Add‑Ins** → **COM Add‑ins → Go…**  
4. Check **Aspose.Cells Reporting Services Designer** and click **OK**.

## 📂 4. Deploy the Rendering Extension to SSRS  

### 4.1 Copy the renderer DLL  

Copy the version‑specific `Aspose.Cells.ReportingServices.dll` to the SSRS **bin** folder:

```text
%ProgramFiles%\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer\bin
```

*(Path varies with SSRS version – replace `MSRS13.MSSQLSERVER` with your instance name.)*

### 4.2 Register the renderer in `rsreportserver.config`  

Edit the file:

```
%ProgramFiles%\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer\rsreportserver.config
```

Locate the `<Render>` element and insert the following entries **inside** it (keep existing extensions intact):

```xml
<!-- Aspose.Cells for Reporting Services renderers -->
<Extension Name="ACXLS"       Type="Aspose.Cells.ReportingServices.XlsRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACXLSX"      Type="Aspose.Cells.ReportingServices.Excel2007XlsxRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACXLSX(Data Only)" Type="Aspose.Cells.ReportingServices.Excel2007SimpleXlsxRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACXLSB"      Type="Aspose.Cells.ReportingServices.XlsbRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACXLSM"      Type="Aspose.Cells.ReportingServices.Excel2007XlsmRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACXML"       Type="Aspose.Cells.ReportingServices.SpreadsheetMLRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACHTML"      Type="Aspose.Cells.ReportingServices.HtmlRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACCSV"       Type="Aspose.Cells.ReportingServices.CSVRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACODS"       Type="Aspose.Cells.ReportingServices.ODSRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACTXT"       Type="Aspose.Cells.ReportingServices.TabDelimitedRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACXPS"       Type="Aspose.Cells.ReportingServices.XpsRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACMD"        Type="Aspose.Cells.ReportingServices.MarkdownRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACTIFF"      Type="Aspose.Cells.ReportingServices.TIFFRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACPDF"       Type="Aspose.Cells.ReportingServices.PDFRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACPNG"       Type="Aspose.Cells.ReportingServices.PNGRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACJPG"       Type="Aspose.Cells.ReportingServices.JPGRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACEMF"       Type="Aspose.Cells.ReportingServices.EMFRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACDIF"       Type="Aspose.Cells.ReportingServices.DifRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACSVG"       Type="Aspose.Cells.ReportingServices.SvgRenderer, Aspose.Cells.ReportingServices" />
<Extension Name="ACJSON"      Type="Aspose.Cells.ReportingServices.JsonRenderer, Aspose.Cells.ReportingServices" />
```

> **Tip:** Preserve the original indentation and line‑break style to keep the file readable.

### 4.3 Grant Full‑Trust to the assembly  

Edit **`rssrvpolicy.config`** (same folder as `rsreportserver.config`) and add a new `CodeGroup` that grants **FullTrust** to the Aspose.Cells assembly.

Locate the outer `<CodeGroup>` with `PermissionSetName="Execution"` and insert the following **as the last child**:

```xml
<!-- Aspose.Cells for Reporting Services – Full Trust -->
<CodeGroup class="UnionCodeGroup" version="1"
           PermissionSetName="FullTrust"
           Name="Aspose.Cells_for_Reporting_Services"
           Description="Grants full trust to Aspose.Cells for Reporting Services assemblies">
  <IMembershipCondition class="StrongNameMembershipCondition" version="1"
    PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001002780c08eaa89aedfb00b1b96137cca3e15f32826e0e4fd1da3c98d1e3968a03a019aa7b7228b151f6e5dae4dcb00f98479770f507626b04e786e5e93ec3757c1cc4ed1ac4b72c7649c4438e9d3a5f44d8b7522043686a2e8c2a495e04b917e0505d3201015c828e3c15afc8a46ab78293574b9e0475df68627bbabc5b564addd" />
</CodeGroup>
```

> **Why?** The renderer runs inside the SSRS sandbox; FullTrust is required for file‑system and native‑code access.

---

## ✅ 5. Verify the Installation  

1. Open **Report Manager** (default URL: `http://<ServerName>/Reports`).  
2. Navigate to any report and click **Export** → **Select Format**.  
3. You should see a list of new formats prefixed with **“AC”** (e.g., **ACXLS – Excel Workbook via Aspose.Cells**).  
4. Choose a format (e.g., **ACXLSX**) and click **Export**.  
5. The report is generated and downloaded. Open it in Microsoft Excel to confirm the output.

If the new formats are missing, double‑check:

* The DLL is in the correct `ReportServer\bin` folder.  
* The `<Extension>` entries are inside the `<Render>` element (no stray tags).  
* The `CodeGroup` was added correctly and the XML is well‑formed.  
* IIS/SSRS service was restarted (or simply run `net stop ReportServer && net start ReportServer`).

## Verify that Aspose.Cells for Reporting Services is installed successfully

   1. Open the Report Manager and check the list of available export types for a report. Launch Report Manager by opening a browser and type the Report Manager URL into the address bar. (By default, the URL is http://<ComputerName>/Reports).
   1. Select one of the reports on the server and open the **Select Format** list.
      You should see the list of export formats provided by Aspose.Cells for Reporting Services.
   1. Select **XLS – Excel Workbook via Aspose.Cells**.
   1. Click **Export**.
      The report is generated in the selected format.
   1. Send it to the client and open it in an appropriate application. In this case, the report opens in Microsoft Excel.

Congratulations, you’ve successfully installed Aspose.Cells for Reporting Services and generated a report as a Microsoft Excel file!

There are 7 kinds of versions Aspose.Cells.ReprotingSerivces.dll in Aspose.Cells.ReportingServices.DLLs_xx.xx.zip. They support different Microsoft report server products.
