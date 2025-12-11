---
title: How to Format Number to Accounting with Golang via C++
linktitle: How to Format Number to Accounting
type: docs
weight: 10
url: /go-cpp/how-to-format-number-to-accounting/
description: This article introduces how to format numbers to accounting using the Aspose.Cells for C++ API.
keywords: Convert numerical values into an accounting format, Apply accounting formatting to numeric data, Transform numbers into an accounting representation, Format figures according to accounting standards, Adjust numerical entries to follow accounting format conventions, Format Number to Accounting
---

## **Possible Usage Scenarios**
Formatting numbers to accounting in Excel is a common practice for several reasons, especially in business, finance, and accounting fields. This formatting style provides a standardized way of presenting numerical data, making it easier to read, understand, and compare. Here are some key reasons why you might format numbers to accounting in Excel:

1. **Uniformity and Professionalism**: The accounting format aligns the currency symbols and decimal points in a column, providing a clean and professional appearance. This uniformity helps in presenting financial data in a more structured and appealing way, which is crucial for reports and presentations.

2. **Clarity and Precision**: By displaying numbers in a consistent format, including the use of commas for thousands and specifying the number of decimal places, the accounting format enhances clarity and precision. This is particularly important for financial analysis and decision‑making, where accuracy is paramount.

3. **Negative Numbers Representation**: The accounting format typically represents negative numbers in parentheses rather than using a minus sign. This convention is widely used in accounting and finance to make negative values stand out more clearly, reducing the risk of overlooking them.

4. **Zero Values Representation**: In accounting format, zero values are often represented as a dash (‑) instead of a numeral zero (0). This practice helps distinguish between zero values and cells that are empty or have not been filled in, adding to the clarity of the data presented.

5. **Currency Symbol**: The accounting format allows for the inclusion of a currency symbol directly in the cell with the number. This is particularly useful in financial documents where it is important to indicate the currency of the amounts being discussed, especially in international contexts where multiple currencies might be involved.

6. **Ease of Comparison**: When financial data is formatted consistently using the accounting format, it becomes easier to compare figures across different rows, columns, or even separate documents. This can aid in analyzing trends, making forecasts, and identifying discrepancies.

7. **Compliance and Standards**: In many cases, the use of the accounting format is not just a preference but a requirement. Certain financial reporting standards and practices may dictate the use of this format for presenting financial statements and other accounting documents.

In summary, formatting numbers to accounting in Excel is a critical practice for anyone dealing with financial data. It enhances the presentation, clarity, and usability of numerical information, which is essential for effective analysis, reporting, and decision‑making in the business and finance sectors.

## **How to Format Number to Accounting in Excel**
Formatting numbers to display in accounting format in Excel is a straightforward process. The accounting format aligns the currency symbols and decimal points in a column, making it easier to read financial statements. It also displays negative numbers in parentheses. Here's how you can format numbers to accounting in Excel:

### Using the Ribbon

1. **Select the Cells**: First, select the cells or range of cells that you want to format.  
2. **Open the Format Cells Dialog**:  
   - Right‑click on the selected cells and choose **Format Cells**, or  
   - Go to the **Home** tab on the ribbon, locate the **Number** group, and click the small arrow in the bottom‑right corner to open the **Format Cells** dialog box. Alternatively, press **Ctrl + 1** to open the dialog.  
3. **Choose Accounting Format**:  
   - In the **Format Cells** dialog box, click the **Number** tab.  
   - In the list on the left, select **Accounting**.  
   - Choose the specific settings you want, such as the currency symbol and the number of decimal places.  
   - Click **OK** to apply the formatting.

### Using the Ribbon's Shortcut

For a quicker method, you can also use the ribbon’s shortcut buttons:

1. **Select the Cells**: Highlight the cells you want to format.  
2. **Go to the Home Tab**: On the **Home** tab, in the **Number** group, click the dropdown for number formats.  
3. **Select Accounting Format**: Choose **Accounting Number Format**. This automatically applies the default accounting format to your selected cells.

### Customizing the Accounting Format

If you need a specific type of accounting format (for example, without a currency symbol or with a different number of decimal places), you can customize it:

1. **Open the Format Cells Dialog**: Follow the steps above to open the dialog.  
2. **Choose Accounting and Customize**: After selecting **Accounting**, adjust the decimal places or select a different symbol. If you don’t want any symbol, select **None**.

### Using Excel's Accounting Format vs. Custom Number Format

While the accounting format is designed for financial statements and aligns currency symbols and decimal points, you may sometimes need more customization. In such cases, consider using the **Custom** number format (accessible in the **Format Cells** dialog under the **Number** tab). This allows you to create a format that exactly meets your needs, though it requires familiarity with Excel’s custom format codes.

### Conclusion

Formatting numbers as accounting in Excel helps present financial data more clearly and professionally. Whether you’re preparing financial statements or managing budgets, using the accounting format can make your data easier to read and understand.

## **How to Format Number to Accounting in Aspose.Cells for C++**
To format numbers to accounting format in Aspose.Cells for C++, you can use the `Style` object associated with a cell or range of cells. The `Style` object allows you to set various formatting options, including number formats. The accounting format typically has a format code that can vary depending on the specific requirements (such as whether to show currency symbols, decimal places, etc.).

Here’s a basic example of how to apply an accounting number format to a cell in Aspose.Cells for C++:

1. **Reference Aspose.Cells**: Ensure that Aspose.Cells for C++ is referenced in your project. You can obtain it from the Aspose website.  
2. **Create or Open a Workbook**: Create a new workbook or open an existing one.  
3. **Access the Desired Cell**: Identify and access the cell or range of cells you want to format.  
4. **Apply Accounting Format**: Set the number format of the cell’s style to an accounting format.  
5. **Sample Code**: Below is a code snippet demonstrating these steps.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FormatNumberToAccounting.go" >}}

This example demonstrates how to format a single cell to display numbers in an accounting format with US dollars. The format string can be adjusted to meet different currency symbols or accounting formats as needed. The key part is the `style.Custom` property, where you specify the custom number format code for accounting.

Remember, the exact format string might need to be adjusted based on your locale and the specific accounting format requirements you have (e.g., using a different currency symbol, showing more or fewer decimal places, etc.).