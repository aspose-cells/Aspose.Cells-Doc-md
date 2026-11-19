---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells Java
description: Learn how to render array data into a single cell using the arrayassingle and arraydelimiter Smart Marker attributes in Aspose.Cells for Java.
linktitle: SmartMarker Single Cell Array Rendering | Aspose.Cells
url: /java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Java library, spreadsheet, Smart Markers, arrayassingle, arraydelimiter, single cell array, array rendering, template
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells can render an array data source into one single cell through Smart Markers. The `arrayassingle` attribute turns off the default element-by-element spreading, and the `arraydelimiter` attribute chooses the separator placed between the joined elements — comma by default, or any single character or quoted multi-character string you specify.
{{% /alert %}}

## **Introduction**
Smart Markers in Aspose.Cells are a template-based feature that populates spreadsheet data dynamically using marker expressions such as `&=DataSource.Field`. The marker is placed in a designer workbook, and when the template is processed by the `WorkbookDesigner`, the markers are replaced with values from the supplied data source.
By default, when a Smart Marker references an array property (for example, `&=Product.Tags` bound to a `String[]` of four values), the engine expands the array and places each element into its own cell, spreading the values vertically down the column below the marker. While this behavior is convenient in many scenarios, there are situations where you would prefer to render the entire array into one single cell, with the elements concatenated and separated by a delimiter of your choice.
The `arrayassingle` and `arraydelimiter` attributes, written inside a Smart Marker's parentheses in `name:value` form, address exactly this requirement. They allow you to keep report layouts compact and predictable while still working natively with array data sources.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
When a Smart Marker references an array property, Aspose.Cells expands the array across multiple cells by default. For example, a marker such as `&=Product.Tags` against a `String[]` containing four values places each value into its own cell below the marker, pushing other template content outward and potentially breaking carefully designed report layouts.

### **Use Case Limitations**
There are many practical scenarios where the default spreading behavior is undesirable:
- **Summary-style reports** that need a compact one-row-per-record layout.
- **Tag, label, or keyword lists** that need to be displayed as comma-separated or pipe-separated values within a single cell.
- **Filter chips or status indicators** that group multiple values in one place for readability.
- **Downstream pipelines** (CSV export, PDF rendering, mail merge) that expect a single consolidated value per cell rather than an expanded range.
- **Cross-platform compatibility**, where some consumers cannot tolerate arrays that bleed across multiple cells.

### **The Gap It Fills**
Without a built-in mechanism, developers would be forced to pre-process data in Java — joining arrays into delimited strings before binding them to the workbook designer. This duplicates logic, complicates data models, and increases the chance of errors. The `arrayassingle` and `arraydelimiter` attributes eliminate this workaround by handling the formatting declaratively inside the Smart Marker itself.

## **Feature Benefits**
Using the `arrayassingle` and `arraydelimiter` attributes in your Smart Markers provides several advantages:
- **Single-cell containment**: All array elements are rendered into exactly one cell, keeping layouts compact and predictable.
- **Custom delimiter control**: Specify the separator you like — the default comma, a semicolon, a hyphen, a pipe, or a quoted multi-character string such as `" | "`.
- **Template-driven formatting**: No additional code is required to pre-process the data; formatting rules live inside the Smart Marker tag.
- **Cleaner reports**: Array data no longer pushes neighboring template content into different rows or columns.
- **Versatile data types**: Works with string arrays and string-rendered numeric values from bean data sources.
- **Backwards compatibility**: When the attributes are omitted, the original spreading behavior is preserved, so existing templates continue to work unchanged.

## **How to Use This Feature**

### **Smart Marker Syntax**
The `arrayassingle` and `arraydelimiter` attributes use Aspose.Cells' `name:value` attribute grammar inside the parentheses of a standard Smart Marker. The general syntax is:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

The marker is composed of the following parts:
- `&=DataSource.ArrayProperty` — the standard Smart Marker referencing the array property on the bound data source.
- `arrayassingle:true` — instructs the engine to render the whole array into a single cell instead of spreading the elements.
- `arraydelimiter:;` — optional; defines the separator placed between array elements. When it is omitted, a comma is used.

{{% alert color="warning" %}}
Write attributes in `name:value` form (a colon, not an equals sign) and separate multiple attributes with a comma **without spaces**. A space after the comma shifts the parsed value by one character — `(arrayassingle:true, arraydelimiter:;)` would join with the erroneous separator `:;` instead of `;`.
{{% /alert %}}

### **Delimiter Forms**
- A single character follows the colon directly: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- A multi-character separator is written in double quotes: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Step-by-Step Workflow**
The following workflow describes how to render an array into a single cell using Smart Markers.
1. **Prepare the data source**: Create a `public` bean class with a getter returning the array, such as `String[] getTags()`, and bind a `java.util.List` of beans so the engine reads one record per row. Public fields alone do not bind — the engine reads JavaBean getters.
2. **Create a designer workbook**: Create a new `Workbook`, add a header row, and place a Smart Marker cell that references the array property with the `arrayassingle` attribute (and `arraydelimiter` when a custom separator is needed).
3. **Instantiate the WorkbookDesigner**: Create a `WorkbookDesigner` around the workbook and bind your list with `setDataSource`.
4. **Process the markers**: Call the `WorkbookDesigner.process()` method to expand the Smart Markers and populate the workbook with real data.
5. **Save the result**: Save the resulting workbook to disk in XLSX or any other supported file format.

### **Code Example 1 — Basic String Array Rendering**

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

The example prints the joined value of the whole array. The four tags land in one cell, separated by the default comma:

```
C#,Aspose,SmartMarker,Excel
```

### **Code Example 2 — Numeric Values with a Custom Delimiter**

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }
    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

Numeric values join exactly like strings when the array property returns `String[]`:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Keep the array property a `String[]` on Java. A primitive `int[]` property joined into a single cell renders the array object's toString text (for example `[I@1a2b3c4d`) instead of the numbers, because the join operates on each element's string form and a primitive array is one opaque element.
{{% /alert %}}

### **Code Example 3 — Comparing Default vs. Single-Cell Rendering**

```java
import com.aspose.cells.*;
import java.util.*;
public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }
    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

The default marker fills one cell per element down column B, while the `arrayassingle` marker collapses the same array into a single cell in column C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notes & Best Practices**
Keep the following points in mind when working with the `arrayassingle` and `arraydelimiter` attributes:
- Attribute values use the `name:value` form. An equals-sign form such as `arrayassingle=true` is not recognized and silently falls back to the default spreading behavior.
- Separate attributes with a comma and no spaces; a space after the comma shifts the delimiter value by one character (see the warning above).
- The `arraydelimiter` value may be a single character written directly after the colon, or a multi-character string wrapped in double quotes.
- When `arraydelimiter` is omitted, elements are joined with a comma.
- Bind a `java.util.List` of public JavaBeans with array getters. A single bean object or public fields alone leave the markers unresolved.
- Keep array properties as `String[]`; a primitive `int[]` renders its toString text when joined (see the note above).
- Place the Smart Marker in a cell that has sufficient width to display the resulting concatenated string; otherwise, the content may visually overflow into adjacent cells depending on the format.

## Related Articles
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Java](/cells/java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Java](/cells/java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/java/change-page-field-layout/)
- [Convert Sparkline to Image and HTML in Aspose.Cells for Java](/cells/java/convert-sparkline-to-image-and-html/)
- [Converting Excel to OFD Format](/cells/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}