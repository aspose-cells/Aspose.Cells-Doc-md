---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells Java
description: Learn how to render array data into a single cell using the ArrayAsSingle and ExtraDelimiter attributes in Smart Markers with Aspose.Cells for Aspose.Cells for Java.
keywords: Aspose.Cells, Java library, spreadsheet, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, array rendering, template
type: docs
weight: 195
url: /java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells supports rendering array data into a single cell via Smart Markers. By using the `ArrayAsSingle` attribute along with the `ExtraDelimiter` attribute, developers can control how array elements are separated within a single cell, providing flexible formatting for reports and templates.

{{% /alert %}}

## **Introduction**

Smart Markers in Aspose.Cells are a powerful, template-based feature that allows you to dynamically populate spreadsheet data using marker expressions such as `&=DataSource.Field`. The marker is placed in a designer workbook, and when the template is processed by the `WorkbookDesigner`, the markers are replaced with values from the supplied data source.

By default, when a Smart Marker references an array property (for example, `&=DataSource.Numbers`), the engine expands the array and places each element into a separate adjacent cell — either horizontally across a row or vertically down a column. While this behavior is convenient in many scenarios, there are situations where you would prefer to render the entire array into one single cell, with the elements concatenated and separated by a delimiter of your choice.

The `ArrayAsSingle` and `ExtraDelimiter` attributes, used together inside a Smart Marker tag, address exactly this requirement. They allow you to keep report layouts compact and predictable while still working natively with array data sources.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**

When a Smart Marker references an array property, Aspose.Cells expands the array across multiple cells by default. For example, a marker such as `&=Product.Tags` against a `string[]` containing four values will place each value into its own cell, pushing other template content outward and potentially breaking carefully designed report layouts.

### **Use Case Limitations**

There are many practical scenarios where the default spreading behavior is undesirable:

- **Summary-style reports** that need a compact one-row-per-record layout.
- **Tag, label, or keyword lists** that need to be displayed as comma-separated or pipe-separated values within a single cell.
- **Filter chips or status indicators** that group multiple values in one place for readability.
- **Downstream pipelines** (CSV export, PDF rendering, mail merge) that expect a single consolidated value per cell rather than an expanded range.
- **Cross-platform compatibility**, where some consumers cannot tolerate arrays that bleed across multiple cells.

### **The Gap It Fills**

Without a built-in mechanism, developers would be forced to pre-process data in Java — joining arrays into delimited strings before binding them to the workbook designer. This duplicates logic, complicates data models, and increases the chance of errors. The `ArrayAsSingle` and `ExtraDelimiter` attributes eliminate this workaround by handling the formatting declaratively inside the Smart Marker itself.

## **Feature Benefits**

Using the `ArrayAsSingle` and `ExtraDelimiter` attributes in your Smart Markers provides several advantages:

- **Single-cell containment**: All array elements are rendered into exactly one cell, keeping layouts compact and predictable.
- **Custom delimiter control**: Specify any separator string you like — comma, semicolon, hyphen, pipe, newline, or any custom text.
- **Template-driven formatting**: No additional code is required to pre-process the data; formatting rules live inside the Smart Marker tag.
- **Cleaner reports**: Array data no longer pushes neighboring template content into different rows or columns.
- **Versatile data types**: Works with strings, numbers, dates, and any other data type that can be joined with a delimiter.
- **Backwards compatibility**: When the attributes are omitted, the original spreading behavior is preserved, so existing templates continue to work unchanged.

## **How to Use This Feature**

### **Smart Marker Syntax**

The `ArrayAsSingle` and `ExtraDelimiter` attributes are passed as key-value pairs inside the parentheses of a standard Smart Marker. The general syntax is:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

The marker is composed of the following parts:

- `&=DataSource.ArrayProperty` — the standard Smart Marker referencing the array property on the bound data source.
- `arrayasSingle=true` — instructs the engine to render the whole array into a single cell. Only the value `true` triggers the single-cell behavior.
- `extraDelimiter=", "` — defines the separator placed between array elements. The value is a string literal; it can be empty, a single character, or a multi-character string.

{{% alert color="primary" %}}

The `extraDelimiter` attribute accepts any string literal, including multi-character delimiters, custom text, or escape sequences such as `\n` for newline-separated output. If the array is empty, the resulting cell is left blank.

{{% /alert %}}

### **Step-by-Step Workflow**

The following workflow describes how to render an array into a single cell using Smart Markers.

1. **Prepare the data source**: Create a class (or data structure) that exposes a property returning an array. The property can return `String[]`, `int[]`, or any other supported array type.
2. **Create a designer workbook**: Create a new `Workbook`, add a header row, and place a Smart Marker cell that references the array property with the `arrayasSingle` and `extraDelimiter` attributes.
3. **Instantiate the WorkbookDesigner**: Create a `WorkbookDesigner` object, attach the designer workbook to it, and bind your data source using the `setDataSource` method.
4. **Process the markers**: Call the `WorkbookDesigner.process()` method to expand the Smart Markers and populate the workbook with real data.
5. **Save the result**: Save the resulting workbook to disk in XLSX or any other supported file format.

### **Code Example 1 — Basic String Array Rendering**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **Notes & Best Practices**

Keep the following points in mind when working with the `ArrayAsSingle` and `ExtraDelimiter` attributes:

- The `extraDelimiter` value is treated as a string literal; escape any special characters that your template processor might interpret.
- The `arrayasSingle` attribute accepts a boolean value (`true` / `false`). Only `true` triggers the single-cell behavior; any other value falls back to the default spreading behavior.
- If the array is empty or null, the cell is left empty (or contains a blank string depending on the data type).
- The feature works with object data sources as well as `DataSet` and `DataTable` sources where a column can be split into arrays.
- For newline-separated output, you can use `\n` or `System.lineSeparator()` as the delimiter value.
- Place the Smart Marker in a cell that has sufficient width to display the resulting concatenated string; otherwise, the content may visually overflow into adjacent cells depending on the format.

## **Related Articles**

- [Smart Markers](/cells/java/smart-markers/)
- [Merging and Unmerging Cells](/cells/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}