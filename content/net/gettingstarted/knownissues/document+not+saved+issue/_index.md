---
title : "Document Not Saved Issue" 
description : "" 
weight : 12026 
toc : false
type: docs
url: /net/gettingstarted/knownissues/document+not+saved+issue/
---

# Aspose.Cells for .NET : Document Not Saved Issue


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Issue](#issue)
    *   1.1 [Issue Summary](#issue-summary)
    *   1.2 [Symptom](#symptom)
    *   1.3 [Causes](#causes)
    *   1.4 [Solution](#solution)
{{< /panel >}}
## Issue

I am having a strange problem with a spreadsheet I've created with your control. It opens and edits just fine in Excel, but when I try to perform a Save or Save As, I get a "Document Not Saved" msgbox.

### Issue Summary

This is an Excel bug:  
[http://support.microsoft.com/default.aspx?scid=kb;en-us;121942&Product=xlw97](http://support.microsoft.com/default.aspx?scid=kb;en-us;121942&Product=xlw97)

"Document Not Saved" Saving File Created from Template

Article ID : 121942

Last Review : August 15, 2005

Revision : 1.3

This article was previously published under Q121942

### Symptom

When you attempt to save a workbook, you may receive the following error message: **"Document Not Saved"**

### Causes

This problem may occur when the following conditions are true:

*   The workbook was created from a template that contained an embedded object.
*   You have inserted a worksheet into your workbook from a template.
*   The template contains an embedded object.

### Solution

To save your work, you must first delete the embedded objects in your workbook.

