---
title: Document Not Saved Issue
type: docs
weight: 40
url: /net/document-not-saved-issue/
---

## **Issue**
I am having a strange problem with a spreadsheet I've created with your control. It opens and edits just fine in Excel, but when I try to perform a Save or Save As, I get a "Document Not Saved" msgbox.
### **Issue Summary**
This is an Excel bug: 

"Document Not Saved" Saving File Created from Template

Article ID : 121942

Last Review : August 15, 2005

Revision : 1.3

This article was previously published under Q121942
### **Symptom**
When you attempt to save a workbook, you may receive the following error message: **"Document Not Saved"**
### **Causes**
This problem may occur when the following conditions are true:

- The workbook was created from a template that contained an embedded object.
- You have inserted a worksheet into your workbook from a template.
- The template contains an embedded object.
### **Solution**
To save your work, you must first delete the embedded objects in your workbook.
