##Preserve Single Quote Prefix of Cell Value or Range
Learn how to Preserve Single Quote Prefix of Cell Value or Range through the Aspose.Cells for .NET API.
## **Possible Usage Scenarios**
When you put some value inside the cell that has leading apostrophe or single quote mark, then Microsoft Excel hides it, but when you select the cell, it displays the leading apostrophe or single quote in a formula bar as shown in the following screenshot.
![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)
Aspose.Cells also hides the leading apostrophe or single quote like Microsoft Excel but it sets the [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) as **true** for that cell. If you set an empty style of the cell, then [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) becomes **false** again. In order to deal with this issue, Aspose.Cells provides [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) property, when it is set **false**, then [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) is not updated at all and its old value is preserved. It means if the old value of [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) property was **true**, it will remain **true** and if the old value was **false**, it will remain **false**.
## **Preserve Single Quote Prefix of Cell Value or Range**
The following sample code explains the usage of [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) property as described previously. Please read the comments inside the code and see the console output of the code given below for more help.
## **Sample Code**
## **Console Output**
Quote Prefix of Cell A1: False
Quote Prefix of Cell A1: True
When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.
Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.
Quote Prefix of Cell A1: True
Quote Prefix of Cell A1: False
