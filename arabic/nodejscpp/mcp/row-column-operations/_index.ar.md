---
title: عمليات الصف والعمود في إكسل
linktitle: عمليات الصف والعمود
type: docs
weight: 50
url: /ar/nodejs-cpp/mcp/row-column-operations
keywords: "عمليات صفوف إكسل، عمليات أعمدة إكسل، إدارة تخطيط إكسل، إدراج صفوف، حذف أعمدة، تغيير حجم خلايا إكسل"
description: "عمليات الصف والعمود في إكسل  إدراج، حذف، تغيير حجم، إخفاء/إظهار الصفوف والأعمدة باستخدام الأتمتة بالذكاء الاصطناعي"
---

# عمليات الصف والعمود في إكسل

إدارة **عمليات الصف والعمود في إكسل** باستخدام الأتمتة المدعومة بالذكاء الاصطناعي. أدخل، احذف، غير حجم، أخفي/اظهر **صفوف إكسل** و **أعمدة إكسل** لتحقيق إدارة مثالية لتخطيط جداول البيانات.

## الأدوات المتاحة

- `row_column_operations` - **عمليات صفوف/أعمدة إكسل** (إدراج، حذف، تغيير حجم، إخفاء/إظهار) مع **Excel الذكي**
- `row_column_operations_batch` - تنفيذ عدة **عمليات صفوف/أعمدة إكسل** دفعة واحدة باستخدام **Excel MCP**

## العمليات الفردية

### إدراج صفوف
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/layout-test.xlsx",
    "sheet_name": "Data",
    "operation": "insert_rows",
    "rows": "5",
    "count": 2
  }
}
```

### حذف أعمدة
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Sheet1",
    "operation": "delete_columns",
    "columns": "C:D"
  }
}
```

### ضبط ارتفاع الصف
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_row_height",
    "rows": "1",
    "height": 30
  }
}
```

### تعيين عرض العمود
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "reports/formatted.xlsx",
    "sheet_name": "Report",
    "operation": "set_column_width",
    "columns": "A:F",
    "width": 15
  }
}
```

## عمليات الدُفعة

### إعداد التخطيط الشامل
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/professional-layout.xlsx",
    "sheet_name": "Summary Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "3",
        "height": 30
      },
      {
        "operation": "set_row_height",
        "rows": "4:6",
        "height": 20
      },
      {
        "operation": "set_column_width",
        "columns": "C",
        "width": 20
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      },
      {
        "operation": "auto_fit_rows",
        "rows": "7:10"
      }
    ]
  }
}
```

### عمليات الإدراج والحذف
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/restructure.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "5",
        "count": 2
      },
      {
        "operation": "insert_columns",
        "columns": "D",
        "count": 1
      },
      {
        "operation": "delete_rows",
        "rows": "8:9"
      }
    ]
  }
}
```

### عمليات الإخفاء وإظهار المحتوى
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/visibility.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "hide_rows",
        "rows": "15:16"
      },
      {
        "operation": "hide_columns",
        "columns": "H:I"
      },
      {
        "operation": "unhide_rows",
        "rows": "15"
      },
      {
        "operation": "unhide_columns",
        "columns": "H"
      }
    ]
  }
}
```

### عمليات التكيف التلقائي
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/auto-sized.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "auto_fit_columns",
        "columns": "A:F"
      },
      {
        "operation": "auto_fit_rows",
        "rows": "1:20"
      }
    ]
  }
}
```

## مرجع أنواع العمليات

### عمليات الإدراج
- `insert_rows` - إدراج صفوف جديدة في الموضع المحدد
- `insert_columns` - إدراج أعمدة جديدة في الموضع المحدد

### عمليات الحذف  
- `delete_rows` - حذف الصفوف المحددة
- `delete_columns` - حذف الأعمدة المحددة

### عمليات التغيير بالحجم
- `set_row_height` - ضبط ارتفاع الصف المحدد بالنقاط
- `set_column_width` - ضبط عرض العمود المحدد بالأحرف
- `auto_fit_rows` - التكيف التلقائي لارتفاع الصفوف الذي يناسب المحتوى
- `auto_fit_columns` - التكيف التلقائي لعرض الأعمدة الذي يناسب المحتوى

### عمليات الرؤية
- `hide_rows` - إخفاء الصفوف المحددة
- `unhide_rows` - إظهار الصفوف المخفية
- `hide_columns` - إخفاء الأعمدة المحددة
- `unhide_columns` - إظهار الأعمدة المخفية

## مواصفات المدى

### نطاقات الصفوف
- `"1"` - صف واحد (الصف 1)
- `"1:3"` - نطاق من الصفوف (الصف 1 إلى 3)
- `"5:10"` - عدة صفوف متتالية

### نطاقات الأعمدة
- `"A"` - عمود واحد (العمود أ)
- `"A:C"` - نطاق من الأعمدة (الأعمدة أ إلى ج)
- `"D:F"` - عدة أعمدة متتالية

## أمثلة متقدمة

### إعداد رأس التقرير
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/header-setup.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "set_row_height",
        "rows": "1:2",
        "height": 35
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 25
      },
      {
        "operation": "set_column_width",
        "columns": "B:E",
        "width": 12
      },
      {
        "operation": "set_column_width",
        "columns": "F",
        "width": 18
      }
    ]
  }
}
```

### تنسيق جدول البيانات
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/data-table.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "insert_rows",
        "rows": "1",
        "count": 1
      },
      {
        "operation": "set_row_height",
        "rows": "1",
        "height": 25
      },
      {
        "operation": "auto_fit_columns",
        "columns": "A:J"
      },
      {
        "operation": "set_row_height",
        "rows": "2:100",
        "height": 18
      }
    ]
  }
}
```

### تنسيق العرض التقديمي
```json
{
  "tool": "row_column_operations_batch",
  "parameters": {
    "filepath": "reports/presentation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "hide_columns",
        "columns": "B:C"
      },
      {
        "operation": "hide_rows",
        "rows": "10:15"
      },
      {
        "operation": "set_column_width",
        "columns": "A",
        "width": 30
      },
      {
        "operation": "set_column_width",
        "columns": "D:G",
        "width": 15
      }
    ]
  }
}
```

## إرشادات القياس

### ارتفاع الصفوف (نقاط)
- `15` - ارتفاع الصف الافتراضي
- `20` - أعلى قليلاً لسهولة القراءة
- `25` - مثالي للرؤوس
- `30` - رؤوس كبيرة
- `40` - كبير جدًا للعناوين

### عرض الأعمدة (حروف)
- `8` - أعمدة ضيقة (تواريخ، رموز)
- `12` - أعمدة البيانات القياسية
- `15` - أعمدة نص متوسطة الحجم
- `20` - أعمدة نص واسعة
- `25` - عرض إضافي للوصف
- `30` - عرض كبير جدًا للنص الطويل

## أفضل الممارسات

1. **حجم الرأس**: اجعله أعلى وأوسع للتأكيد
2. **تنا consistency**: استخدم ارتفاع صفوف متسق لصفوف البيانات
3. **الملاءمة التلقائية**: استخدم الملاءمة التلقائية لحجم المحتوى الديناميكي
4. **إخفاء غير المستخدم**: اخفِ الصفوف / الأعمدة الفارغة لمظهر أنظف
5. **التجميع المنطقي**: قم بتجميع عمليات تغيير الحجم ذات الصلة في دفعات

## أنماط شائعة

### نمط إعداد التقرير
1. أدخل صفوف العنوان في الأعلى
2. اضبط ارتفاع صف الرأس
3. تلقائي توافق أعمدة البيانات
4. تعيين ارتفاع صف البيانات القياسي
5. إخفاء المناطق غير المستخدمة

### نمط استيراد البيانات
1. إدراج صفوف للبيانات الجديدة
2. التوافق التلقائي للأعمدة مع المحتوى
3. توحيد ارتفاع الصفوف
4. إخفاء أعمدة الحسابات

### نمط العرض التقديمي
1. إخفاء صفوف/أعمدة التفاصيل
2. تكبير مناطق الملخص
3. تعيين أبعاد مناسبة للعرض التقديمي
4. عرض البيانات ذات الصلة فقط

## معالجة الأخطاء

### نطاق الصف غير صحيح
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1", 
    "operation": "set_row_height",
    "rows": "0",
    "height": 20
  }
}
```
**النتيجة**: خطأ - يبدأ أرقام الصفوف من 1

### نطاق العمود غير صحيح
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_column_width", 
    "columns": "ZZ",
    "width": 10
  }
}
```
**النتيجة**: قد ينجح لكنه يتجاوز الاستخدام العادي

### المعلمات المطلوبة مفقودة
```json
{
  "tool": "row_column_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "set_row_height",
    "rows": "1"
  }
}
```
**النتيجة**: خطأ - مطلوب معلمة الارتفاع 
{{< app/cells/assistant language="nodejs-cpp" >}}
