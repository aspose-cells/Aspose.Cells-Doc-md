---
title: How to Add Time Periods Conditional Formatting
description: How to use the Aspose.Cells library in C# to apply TimePeriods conditional formatting. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, TimePeriods Conditional Formatting, C#, Conditional, Formatting
type: docs
weight: 70
url: /net/how-to-add-time-periods-conditional-formatting/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Using Time Periods conditional formatting in Excel is super useful when working with dates—it helps you visually track and manage time-based data quickly.
1. Instant Insights on Time-Based Data: Quickly highlight things like Today’s tasks, Last month’s sales, Upcoming deadlines, Next week’s appointments.
1. Better Time Management: Helps you stay on top of due dates, events, or expiring items. Great for project timelines, invoices, or schedules.
1. Automatic Updates: It updates dynamically. If today’s date changes, Excel will update the formatting without you lifting a finger.

1. Visual Clarity: Makes time-sensitive information stand out using colors or bold styles — so it doesn’t get missed.

## **How to Add Time Periods Conditional Formatting Using Excel**
Here's how you can add Time Periods conditional formatting in Excel — super useful for highlighting dates like today, last week, next month, etc.

Steps to Add Time Periods Conditional Formatting:
1. Select the range of date cells you want to format. Example: A2:A50.
1. Go to the Home tab on the ribbon.
1. Click on Conditional Formatting in the Styles group.
1. Hover over Highlight Cells Rules.
1. Click on A Date Occurring...
1. In the dialog box that appears: Use the drop-down to select a time period(Today, Yesterday, Tomorrow, Last 7 days, Last week, Next month, etc.).
1. Choose the format (default is light red fill with dark red text, or click Custom Format to choose your own).
1. Click OK.


## **How to Add Time Periods Conditional Formatting Using Aspose.Cells for .NET**

Aspose.Cells fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. This example demonstrates an exercise for Time Periods conditional formatting with different sets of attributes.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Formatting-Advanced-TimePeriod.cs" >}}

{{< app/cells/assistant language="csharp" >}}
