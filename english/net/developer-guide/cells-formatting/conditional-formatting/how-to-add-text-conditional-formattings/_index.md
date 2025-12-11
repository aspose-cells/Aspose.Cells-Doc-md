---
title: How to Add Text Conditional Formatting
description: How to use the Aspose.Cells library in C# to apply text conditional formatting. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, Text Conditional Formatting, C#, Conditional, Formatting
type: docs
weight: 70
url: /net/how-to-add-text-conditional-formatting/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Using text‑based conditional formatting in spreadsheets is useful for highlighting cells that meet specific textual criteria. This can improve data analysis and make it easier to find key information in a large dataset. Here are some reasons to use text conditional formatting:

1. Highlight Specific Text: You can apply formatting based on specific words, phrases, or characters. For example, you might want to highlight all cells that contain the word “Urgent” or “Completed” to easily differentiate tasks in a project.  
2. Identify Patterns or Trends: If you’re working with categories or statuses (like “High”, “Medium”, “Low”), text conditional formatting can visually distinguish between them, making it easier to track progress or prioritize tasks.  
3. Error or Data Entry Alerts: Text formatting can flag inconsistent or erroneous entries, such as misspelled words, incomplete text, or incorrect values. This is particularly useful in datasets with a lot of textual input.  
4. Enhanced Readability: Color‑coding text or changing its style (bold, italics, etc.) helps make important information stand out, improving the overall readability of your sheet.  
5. Dynamic Feedback: You can set up rules that automatically adjust the formatting when text matches certain conditions. This means you don’t have to manually update the formatting as the data changes.

In essence, text conditional formatting helps you quickly spot relevant information, errors, and trends, making it a powerful tool for managing and interpreting textual data.

## **How to Add Text Conditional Formatting Using Excel**
To add text‑based conditional formatting in Excel, follow these steps:

1. Select the range of cells: Highlight the cells where you want to apply the conditional formatting.  
2. Open the Conditional Formatting menu: Go to the **Home** tab in the Excel ribbon. Click **Conditional Formatting** in the **Styles** group.  
3. Choose “New Rule”: From the drop‑down menu, select **New Rule**.  
4. Select “Format only cells that contain”: In the **New Formatting Rule** dialog, choose **Format only cells that contain** under the **Select a Rule Type** section.  
5. Set the rule criteria: In the **Format cells with** section, choose **Specific Text** from the drop‑down. Select either **Containing**, **Begins with**, or **Ends with**, depending on the condition you want to apply. Enter the text you want to format (e.g., a specific word like “Urgent” or “Completed”).  
6. Choose the formatting: Click the **Format** button. In the **Format Cells** dialog, you can select the font color, fill color, or any other formatting options you prefer.  
7. Apply the rule: Once you’ve set your desired format, click **OK** to apply the rule. Click **OK** again in the **New Formatting Rule** dialog to close it.  
8. View the results: The cells containing the text you specified will now have the formatting applied, making it easy to spot relevant information.

## **How to Add Text Conditional Formatting Using Aspose.Cells for .NET**

Aspose.Cells fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. These examples demonstrate advanced conditional formatting types including **BeginsWith**, **ContainsBlank**, **ContainsText**, and so on.

### **Format Cell When the Value Starts With Specified Text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-BeginsWith.cs" >}}

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text.cs" >}}

### **Format Cell When the Value Contains Blank**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsBlank.cs" >}}

### **Format Cell When the Value Contains Errors**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsErrors.cs" >}}

### **Format Cell When the Value Contains Specified Text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-ContainsText.cs" >}}

### **Format Cell When the Value Contains Duplicate Values**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-DuplicateValues.cs" >}}

### **Format Cell When the Value Ends With Specified Text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-EndsWith.cs" >}}

### **Format Cell When the Value Does Not Contain Blank**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsBlank.cs" >}}

### **Format Cell When the Value Does Not Contain Errors**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsErrors.cs" >}}

### **Format Cell When the Value Does Not Contain Specified Text**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-NotContainsText.cs" >}}

### **Format Cell When the Value Contains Unique Values**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-Text-UniqueValues.cs" >}}

{{< app/cells/assistant language="csharp" >}}
