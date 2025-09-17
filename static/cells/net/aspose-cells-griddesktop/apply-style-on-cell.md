##Apply Style on cell
This article introduces how to get or set style format  in the cell in the Worksheet in GridDesktop.
This topic deals with applying style format on a cell , we will cover almost every related properties that can be used to apply style on a cell. Besides some basic formatting settings, we will also discuss about drawing borders and setting number format on the cell in detail.
## **Applying a Custom Style on a Cell - An Example**
To change the font and color of a cell using Aspose.Cells.GridDesktop, please follow the steps below:
- Access any desired **Worksheet**
- Access a **Cell** on which we want to apply a **Style**
- Get **Style** of the **Cell**
- Set **Style** properties according to your custom needs
- Finally, set **Style** of the **Cell** with the updated one
There are many useful properties and methods offered by **Style** object that can be used by developers to customize the style according to their requirements. In the code below it is demonstrated that how to apply custom style on cell.
## **Drawing Borders of Cells**
Using **Style** object, we can draw borders of a cell very easily. The borders can be drawn in any color. Moreover, developers also have the flexibility to choose a specific type of line that will be used to draw borders around the cell. Developers can use **SetBorderLine** and **SetBorderColor** methods of **Style** object to draw borders of any type and colors. Similarly, to get border information of any cell, developers can also make use of **GetBorderLine** and **GetBorderColor** methods of **Style** object.
### **Types of Borders**
There are six types of borders supported by Aspose.Cells.GridDesktop as follows:
- **Left** , represents left border
- **Right** , represents right border
- **Top** , represents Top border
- **Bottom** , represents bottom border
- **DiagonalDown** , represents diagonal down border
- **DiagonalUp** , represents diagonal up border
### **Types of Border Lines**
A border is composed of a line. Changing the type of line, changes the appearance of a border. There are many types of border lines supported by Aspose.Cells.GridDesktop, which are also listed below:
- **None** , represents no border
- **Thin** , represents solid line border
- **Medium** , represents solid line border with line width equal to 2f
- **Dashed** , represents dashed line border
- **Dotted** , represents dotted line border
- **Thick** , represents solid line border with line width equal to 3f
- **MediumDashed** , represents dashed line border with line width equal to 2f
- **ThinDashDotted** , represents dash dotted line border
- **MediumDashDotted** , represents dash dotted line border with line width equal to 2f
- **ThinDashDotDotted** , represents dash dot dotted line border
- **MediumDashDotDotted** , represents dash dot dotted line border with line width equal to 2f
## **Summing Up All Together - Example**
## **Setting Number Formats**
Aspose.Cells.GridDesktop also provides kinds of  number formats setting. There are 58 built-in number formats offered by Aspose.Cells.GridDesktop. To see a complete list of all supported number formats, please refer to [Supported Number Formats.](https://docs.aspose.com/cells/net/list-of-supported-number-formats/)
All built-in number formats are assigned an **Index** number. **For example** the **Index** number of **0.00E+00** number format is **11** . To use a built-in number format in any cell, developers can set the NumberFormat property of **Style** object to the **Index** number of that specific number format. However,if developers need to have their own custom number format then they can also use Custom property of **Style** object.
