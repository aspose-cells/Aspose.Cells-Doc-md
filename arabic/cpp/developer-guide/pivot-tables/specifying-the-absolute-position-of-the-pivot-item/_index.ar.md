---
title: تحديد الموقع المطلق لعنصر Pivot باستخدام C++
linktitle: تحديد الموقع المطلق لعنصر الجدول المحوري
type: docs
weight: 50
url: /ar/cpp/specifying-the-absolute-position-of-the-pivot-item/
description: تعلم كيف تحدد الموقع المطلق لعناصر Pivot في C++ باستخدام Aspose.Cells.
---

{{% alert color="primary" %}}

أحيانًا، يحتاج المستخدمون إلى تحديد الموقع المطلق لعناصر Pivot. لقد كشفت واجهة برمجة التطبيقات Aspose.Cells عن بعض الخصائص الجديدة وطريقة لتحقيق هذا المطلب.

- تمت إضافة [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/) الخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في كافة PivotItems بغض النظر عن العقدة الأم. تمت إضافة [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) للخاصية التي يمكن استخدامها لتحديد مؤشر الموقع في PivotItems تحت نفس العقدة الأم.
- أضيفت الطريقة [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) لتحريك العنصر للأعلى أو الأسفل بناءً على قيمة العد، حيث أن العد هو عدد المواقع التي يتم تحريك عنصر Pivot فيها للأعلى أو الأسفل. إذا كانت قيمة العد أقل من الصفر، سيتم تحريك العنصر للأعلى، وإذا كانت أكبر من الصفر، سينتقل عنصر Pivot للأسفل. يُحدد معامل النوع Boolean `isSameParent` ما إذا كانت عملية التحريك يجب أن تُنفذ في نفس العقدة الأصلية أم لا.
- تم إلغاء دعم طريقة `PivotItem.Move(int count)`؛ لذلك يوصى باستخدام الطريقة الجديدة [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/) بدلاً منها.

{{% /alert %}}

يخلق الكود النموذجي التالي جدول Pivot ثم يحدد مواقع عناصر Pivot في نفس العقدة الأصلية. يمكنك تحميل ملف Excel المصدر وملف Excel الناتج للمراجعة. إذا فتحت ملف Excel الناتج، سترى أن عنصر Pivot "4H12" في الموقع 0 في الأصل "K11" و"DIF400" في الموقع 3. وبالمثل، CA32 في الموقع 1 وAAA3 في الموقع 2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb(srcDir + u"source.xlsx");

    // Add new worksheet for pivot table
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet wsPivot = worksheets.Add(u"pvtNew Hardware");
    Worksheet wsData = worksheets.Get(u"New Hardware - Yearly");

    // Get the pivot tables collection for the pivot sheet
    PivotTableCollection pivotTables = wsPivot.GetPivotTables();

    // Add PivotTable to the worksheet
    int index = pivotTables.Add(u"='New Hardware - Yearly'!A1:D621", u"A3", u"HWCounts_PivotTable");

    // Get the PivotTable object
    PivotTable pvtTable = pivotTables.Get(index);

    // Add vendor row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Vendor");

    // Add item row field
    pvtTable.AddFieldToArea(PivotFieldType::Row, u"Item");

    // Add data field
    pvtTable.AddFieldToArea(PivotFieldType::Data, u"2014");

    // Turn off the subtotals for the vendor row field
    PivotField pivotField = pvtTable.GetRowFields().Get(u"Vendor");
    pivotField.SetSubtotals(PivotFieldSubtotalType::None, true);

    // Turn off grand total
    pvtTable.SetShowColumnGrandTotals(false);

    // Refresh and calculate data before modifying pivot items
    pvtTable.RefreshData();
    pvtTable.CalculateData();

    // Set positions for specific pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"4H12").SetPositionInSameParentNode(0);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"DIF400").SetPositionInSameParentNode(3);

    // Recalculate data after modifying pivot items
    pvtTable.CalculateData();

    // Set positions for additional pivot items
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"CA32").SetPositionInSameParentNode(1);
    pvtTable.GetRowFields().Get(u"Item").GetPivotItems().Get(u"AAA3").SetPositionInSameParentNode(2);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

يرجى ملاحظة، أنه من الضروري استدعاء طرق `PivotTable.RefreshData` و `PivotTable.CalculateData` قبل استخدام [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getposition/)، [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/)، و [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}
