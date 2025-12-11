---
title: Page Setup
type: docs
weight: 80
url: /reportingservices/page-setup/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

The configuration includes two sections and eight kinds of Page Setup properties. These properties include **name**, **index**, **FitToPagesTall**, **FitToPagesWide**, **TopMargin**, **FooterMargin**, **HeaderMargin**, **BottomMargin**, **LeftMargin**, and **RightMargin**.

- **name** represents the report name; it represents the whole report when the name is blank.  
- **index** represents the worksheet index of the exported Excel file.  
- **FitToPagesTall** represents the number of pages tall the worksheet will be scaled to when it's printed.  
- **FitToPagesWide** represents the number of pages wide the worksheet will be scaled to when it's printed.  
- **FooterMargin** represents the distance from the bottom of the page to the footer, in the unit of centimeters.  
- **HeaderMargin** represents the distance from the top of the page to the header, in the unit of centimeters.  
- **LeftMargin** represents the size of the left margin, in the unit of centimeters.  
- **RightMargin** represents the size of the right margin, in the unit of centimeters.  
- **TopMargin** represents the size of the top margin, in the unit of centimeters.  
- **BottomMargin** represents the size of the bottom margin, in the unit of centimeters.  

PageSetup Configuration Example:

{{code  lang="xml" }}
<PageSetup>
    <Report name="report name" FitToPagesTall="0" FitToPagesWide="1" TopMargin="1.0" FooterMargin="1.0" HeaderMargin="1.0" BottomMargin="1.0" LeftMargin="1.0" RightMargin="1.0">
        <Sheet index="0" FitToPagesTall="1" FitToPagesWide="1" TopMargin="1.0" FooterMargin="1.0" HeaderMargin="1.0" BottomMargin="1.0" LeftMargin="1.0" RightMargin="1.0"/>
        <Sheet index="1" FitToPagesTall="0" FitToPagesWide="1" TopMargin="1.0" FooterMargin="1.0" HeaderMargin="1.0" BottomMargin="1.0" LeftMargin="1.0" RightMargin="1.0"/>
    </Report>
</PageSetup>
{{code}}
