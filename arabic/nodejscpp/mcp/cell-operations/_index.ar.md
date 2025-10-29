---
title: عمليات خلايا إكسل
linktitle: عمليات الخلايا
type: docs
weight: 60
url: /ar/nodejs-cpp/mcp/cell-operations
keywords: "عمليات خلايا إكسل، دمج خلايا إكسل، نسخ ولصق إكسل، معالجة خلايا إكسل، عمليات خلايا إكسل باستخدام الذكاء الاصطناعي"
description: "عمليات خلايا إكسل  دمج، نسخ/لصق، مسح الخلايا، ومعالجة خلايا متقدمة باستخدام الأتمتة الذكية"
---

# عمليات خلايا إكسل

قم بتنفيذ عمليات خلايا **إكسل متقدمة** باستخدم الأتمتة المدعومة بالذكاء الاصطناعي. دمج الخلايا، عمليات النسخ واللصق، مسح المحتوى، ومعالجة **خلايا إكسل** بدقة.

## الأدوات المتاحة

- `cell_operations` - **عمليات خلايا إكسل** (دمج، نسخ/لصق، مسح) مع **الأتمتة المدعومة بالذكاء الاصطناعي**
- `cell_operations_batch` - تنفيذ عمليات خلايا إكسل متعددة دفعة واحدة من خلال **إدارة جداول البيانات MCP**

## عمليات خلية واحدة

### دمج الخلايا
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/merged-layout.xlsx",
    "sheet_name": "Report",
    "operation": "merge_cells",
    "range": "A1:C1"
  }
}
```

### إلغاء دمج الخلايا
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/unmerged.xlsx",
    "sheet_name": "Data",
    "operation": "unmerge_cells",
    "range": "A1:C1"
  }
}
```

### نسخ الخلايا
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Source",
    "operation": "copy_cells",
    "source_range": "A1:D5"
  }
}
```

### لصق القيم
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/data-copy.xlsx",
    "sheet_name": "Target",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```

### مسح المحتويات
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/cleanup.xlsx",
    "sheet_name": "Data",
    "operation": "clear_contents",
    "range": "A1:Z100"
  }
}
```

## عمليات الخلايا الدُفعية

### إكمال سير العمل للدمج والنسخ
```json
{
  "tool": "cell_operations_batch", 
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Sheet1",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A7:C7"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:F1",
        "destination_range": "A9"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F1", 
        "destination_range": "A12"
      }
    ]
  }
}
```

### عمليات عبر أوراق العمل
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet.xlsx",
    "sheet_name": "Summary",
    "operation": "paste_values",
    "source_range": "A1:F5",
    "source_sheet": "Data",
    "destination_range": "A1"
  }
}
```

### عمليات تنظيف البيانات
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/cleanup-demo.xlsx",
    "sheet_name": "Data",
    "operations": [
      {
        "operation": "clear_contents",
        "range": "A1:A10"
      },
      {
        "operation": "clear_formats",
        "range": "B1:B10"
      },
      {
        "operation": "clear_all",
        "range": "C1:C10"
      }
    ]
  }
}
```

## مرجع أنواع العمليات

### عمليات الدمج
- `merge_cells` - دمج الخلايا في خلية واحدة
- `unmerge_cells` - فصل الخلايا المندمجة مرة أخرى إلى خلايا فردية
- `merge_across` - دمج الخلايا عبر الصفوف مع الاحتفاظ بالصفوف المنفصلة

### عمليات النسخ / اللصق
- `copy_cells` - نسخ نطاق الخلايا إلى الحافظة
- `paste_values` - لصق القيم فقط (بدون تنسيق أو صيغ)
- `paste_formulas` - لصق الصيغ فقط (بدون القيم أو التنسيق)
- `paste_formats` - لصق التنسيق فقط (بدون القيم أو الصيغ)
- `transpose_paste` - اللصق بالتبديل بين الصفوف والأعمدة (الصفوف↔ الأعمدة)

### عمليات المسح
- `clear_contents` - مسح محتوى الخلية (الاحتفاظ بالتنسيق)
- `clear_formats` - مسح تنسيق الخلية (الاحتفاظ بالمحتوى)
- `clear_all` - مسح كل من المحتوى والتنسيقات

## أمثلة متقدمة

### إعداد عنوان التقرير
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/title-report.xlsx",
    "sheet_name": "Report",
    "operations": [
      {
        "operation": "merge_cells",
        "range": "A1:F1"
      },
      {
        "operation": "merge_cells",
        "range": "A2:F2"
      },
      {
        "operation": "merge_cells",
        "range": "A3:C3"
      },
      {
        "operation": "merge_cells",
        "range": "D3:F3"
      }
    ]
  }
}
```

### إنشاء قالب البيانات
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "templates/data-template.xlsx",
    "sheet_name": "Template",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F1"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A10"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A20"
      },
      {
        "operation": "paste_formats",
        "destination_range": "A30"
      }
    ]
  }
}
```

### دمج البيانات
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/consolidated.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q1Data",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q2Data", 
        "destination_range": "A12"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:E10",
        "source_sheet": "Q3Data",
        "destination_range": "A22"
      }
    ]
  }
}
```

### فصل الصيغة والتنسيق
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/separated.xlsx",
    "sheet_name": "Analysis",
    "operations": [
      {
        "operation": "paste_formulas",
        "source_range": "A1:F10",
        "source_sheet": "Calculations",
        "destination_range": "A1"
      },
      {
        "operation": "paste_formats",
        "source_range": "A1:F10", 
        "source_sheet": "Formatting",
        "destination_range": "A1"
      }
    ]
  }
}
```

## عمليات عبر الأوراق

### النسخ بين الأوراق
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/multi-sheet-copy.xlsx",
    "sheet_name": "Destination",
    "operation": "paste_values",
    "source_range": "A1:D10",
    "source_sheet": "Source",
    "destination_range": "B2"
  }
}
```

### إنشاء ورقة ملخصات
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/summary-creation.xlsx",
    "sheet_name": "Summary",
    "operations": [
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "January",
        "destination_range": "A2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "February",
        "destination_range": "E2"
      },
      {
        "operation": "paste_values",
        "source_range": "A1:C5",
        "source_sheet": "March",
        "destination_range": "I2"
      }
    ]
  }
}
```

## تحويل البيانات

### تحويل البيانات إلى صف واحد وعكسها
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "reports/transposed.xlsx",
    "sheet_name": "Data",
    "operation": "transpose_paste",
    "source_range": "A1:E5",
    "destination_range": "G1"
  }
}
```

### نسخ القيم فقط
```json
{
  "tool": "cell_operations_batch",
  "parameters": {
    "filepath": "reports/values-only.xlsx",
    "sheet_name": "Clean Data",
    "operations": [
      {
        "operation": "copy_cells",
        "source_range": "A1:F20",
        "source_sheet": "Raw Data"
      },
      {
        "operation": "paste_values",
        "destination_range": "A1"
      }
    ]
  }
}
```

## أفضل الممارسات

1. **دمج بشكل استراتيجي**: استخدم الدمج للعناوين والعناوين الرئيسية، وليس لمناطق البيانات
2. **نسخ قبل اللصق**: دائمًا انسخ نطاق المصدر قبل عمليات اللصق
3. **مسح بشكل مناسب**: اختر عملية المسح المناسبة لاحتياجاتك
4. **التخطيط بين الأوراق**: خطط لعمليات بين عدة أوراق لتجنب التعارضات
5. **العمليات الجماعية**: مجمّع العمليات ذات الصلة لتحسين الأداء

## الحالات الشائعة للاستخدام

### رؤوس التقارير
- دمج خلايا للعناوين
- نسخ تنسيق الرأس
- تطبيق نمط موحد

### تنظيف البيانات
- مسح المحتوى القديم غير الضروري
- إزالة التنسيق
- إعادة تعيين حالات الخلايا

### إنشاء القوالب
- نسخ أنماط التنسيق
- لصق الهيكل بدون البيانات
- إنشاء تصميمات قابلة لإعادة الاستخدام

### تجميع البيانات
- دمج البيانات من أوراق عمل متعددة
- لصق القيم فقط لتجنب تعارض الصيغ
- تحويل اتجاه البيانات

## معالجة الأخطاء

### نطاق الدمج غير صالح
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "merge_cells",
    "range": "A1"
  }
}
```
**النتيجة**: خطأ - غير قادر على دمج خلية واحدة

### نطاق المصدر مفقود
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "destination_range": "A1"
  }
}
```
**النتيجة**: خطأ - لا توجد بيانات لنسخها

### مرجع ورقة غير صالح
```json
{
  "tool": "cell_operations",
  "parameters": {
    "filepath": "test.xlsx",
    "sheet_name": "Sheet1",
    "operation": "paste_values",
    "source_range": "A1:B2",
    "source_sheet": "NonExistentSheet",
    "destination_range": "A1"
  }
}
```
**النتيجة**: خطأ - لم يتم العثور على ورقة المصدر 
{{< app/cells/assistant language="nodejs-cpp" >}}
