---
title: تحديث العارض باستخدام Golang عبر C++
linktitle: تحديث العارض
type: docs
weight: 50
url: /ar/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: توضح هذه المقالة كيفية تحديث العارض لتصفية بيانات الجدول المحوري أو الجدول المرتبط باستخدام واجهة برمجة التطبيقات Aspose.Cells for Go via C++.
keywords: Aspose.Cells Go via C++ تحديث العارض، كيفية تغيير العارض في Go، كيفية تصفية الجدول المحوري بواسطة العارض في Go، Slicer SelectItems، Slicer ClearFilter، Slicer UnselectItems.
---

## **سيناريوهات الاستخدام المحتملة**
يعني تحديث العارض تصفية بيانات الجدول المحوري أو الجدول المرتبط بالعارض. عندما تحدد عناصر العارض أو تلغي تحديدها في Microsoft Excel، يُعاد حساب الجدول المحوري أو الجدول المرتبط وفقًا لذلك. باستخدام Aspose.Cells for Go via C++، لا تحتاج إلى المرور على عناصر ذاكرة التخزين المؤقت للعارض وتحديث العارض يدويًا — تقوم طريقة [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) بتحديث العارض وإعادة حساب الجدول المحوري أو الجدول المرتبط مباشرةً من عناصر التصفية:
- `Slicer.SelectItems(labels, append)` — تحدد التسميات المطلوبة وتعيد حساب الجدول المحوري أو الجدول المرتبط. عندما تكون قيمة `append` هي `true`، يتم الاحتفاظ بالتسميات المحددة في الأصل وتُضاف التسميات المطلوبة إلى التحديد؛ وعندما تكون قيمة `append` هي `false`، يتم مسح جميع التحديدات الأصلية وتبقى التسميات المطلوبة فقط محددة.
- `Slicer.UnselectItems(labels)` — تلغي تحديد جزء من العناصر المحددة حاليًا.
- `Slicer.ClearFilter()` — تزيل التصفية وتحدد جميع العناصر.

{{% alert color="primary" %}}
بدءًا من Aspose.Cells for Go via C++ 26.10، أصبحت خاصية `SlicerCacheItem.Selected` للقراءة فقط ولم يعد تعيين قيمتها مدعومًا. استخدم الطرق `Slicer.SelectItems` و`Slicer.UnselectItems` و`Slicer.ClearFilter` بدلاً من تعيين `SlicerCacheItem.Selected` عنصرًا بعنصر.
{{% /alert %}}

## **كيفية تحديث العارض**
يقوم الكود النموذجي التالي بتحميل [ملف Excel النموذجي](67338475.xlsx) الذي يحتوي على عارض موجود مرتبط بجدول محوري. يحدد عناصر "Blue" و"Pink" فقط من العارض باستخدام `Slicer.SelectItems(labels, false)` — يُعاد حساب الجدول المحوري مباشرةً من عناصر التصفية دون استدعاء `Slicer.Refresh()` يدويًا. ثم يحفظ المصنف كـ [ملف Excel الناتج](67338476.xlsx). تُظهر لقطة الشاشة التالية تأثير الكود النموذجي على ملف Excel النموذجي. كما يمكنك أن ترى في لقطة الشاشة، يعرض الجدول المحوري العناصر المصفّاة فقط.

## **الكود النموذجي**
استبدل التحديد الحالي (تبقى التسميات المطلوبة فقط محددة) وأعد حساب الجدول المحوري أو الجدول المرتبط:

```go
package main

import (
    "fmt"

    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")

    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)

    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)

    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)

    // Save the modified workbook.
    wb.Save_String("out.xlsx")

    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

احتفظ بالتسميات المحددة حاليًا وحدد عناصر إضافية:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

ألغِ تحديد جزء من العناصر المحددة:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

أزل التصفية (حدد جميع العناصر):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}