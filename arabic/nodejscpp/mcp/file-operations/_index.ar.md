---
title: ملف إكسل وعمليات البيانات
linktitle: ملف وعمليات البيانات
type: docs
weight: 10
url: /ar/nodejs-cpp/mcp/file-operations
keywords: "عمليات ملفات إكسل، عمليات بيانات إكسل، إنشاء دفتر عمل إكسل، ورقة عمل إكسل، قراءة بيانات إكسل، كتابة بيانات إكسل"
description: "عمليات ملفات وبيانات إكسل  إنشاء دفاتر عمل، إدارة أوراق العمل، قراءة وكتابة بيانات إكسل باستخدام الأتمتة بالذكاء الاصطناعي"
---

# عمليات ملفات وبيانات إكسل

إدارة **ملفات إكسل** و **عمليات البيانات** باستخدام الأتمتة المدعومة بالذكاء الاصطناعي. إنشاء **دفاتر عمل إكسل**، إدارة **أوراق العمل**، وأداء عمليات **قراءة وكتابة بيانات إكسل**.

## الأدوات المتاحة

- `create_workbook` - إنشاء دفاتر عمل إكسل جديدة باستخدام أتمتة **AI Excel**
- `create_worksheet` - إضافة **أوراق عمل إكسل** إلى دفاتر عمل إكسل موجودة
- `get_workbook_info` - الحصول على بيانات وصفية ومعلومات عن دفتر عمل إكسل
- `read_data_from_excel` - قراءة البيانات من أوراق إكسل بدقة مدعومة بالذكاء الاصطناعي
- `write_data_to_excel` - كتابة البيانات في أوراق إكسل عبر **Excel MCP**

## إنشاء دفاتر عمل إكسل

### إنشاء دفتر عمل أساسي
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

### إنشاء دفتر عمل مع ورقة مخصصة
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/financial-report.xlsx",
    "sheet_name": "Financial Data"
  }
}
```

## إدارة أوراق العمل

### إضافة ورقة عمل جديدة
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Summary Report"
  }
}
```

### الحصول على معلومات عن دفتر العمل
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/sales-report.xlsx"
  }
}
```

## كتابة بيانات إكسل

### كتابة رؤوس الأعمدة والبيانات
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data",
    "data": [
      ["Product", "Category", "Unit Price", "Quantity", "Total", "Status"],
      ["Laptop Pro", "Electronics", 1299.99, 5, "", "In Stock"],
      ["Wireless Mouse", "Electronics", 89.99, 15, "", "In Stock"],
      ["Office Chair", "Furniture", 299.99, 8, "", "Low Stock"]
    ]
  }
}
```

### كتابة البيانات في الموقع المخصص
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "data": [
      ["Name", "Score", "Grade", "Double Score", "Bonus"],
      ["Alice", 95, "A", "", ""],
      ["Bob", 87, "B", "", ""],
      ["Charlie", 92, "A", "", ""]
    ]
  }
}
```

## قراءة بيانات إكسل

### قراءة النطاق المستخدم بالكامل
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/sales-report.xlsx",
    "sheet_name": "Sales Data"
  }
}
```

### قراءة نطاق محدد
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/analysis.xlsx",
    "sheet_name": "Data Analysis",
    "start_cell": "C3",
    "end_cell": "G6"
  }
}
```

### القراءة من الموقع الافتراضي
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/basic-data.xlsx",
    "sheet_name": "Sheet1",
    "start_cell": "A1"
  }
}
```

## مثال على سير العمل كامل

### 1. إنشاء تقرير إكسل الأول الخاص بك
```json
{
  "tool": "create_workbook",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales"
  }
}
```

### 2. إضافة ورقة الملخص
```json
{
  "tool": "create_worksheet",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Summary"
  }
}
```

### 3. كتابة بيانات المبيعات
```json
{
  "tool": "write_data_to_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "data": [
      ["Month", "Product", "Sales", "Target", "Variance"],
      ["January", "Product A", 5000, 4500, ""],
      ["January", "Product B", 3200, 3000, ""],
      ["February", "Product A", 5500, 4500, ""],
      ["February", "Product B", 3400, 3000, ""]
    ]
  }
}
```

### 4. التحقق من البيانات
```json
{
  "tool": "read_data_from_excel",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx",
    "sheet_name": "Monthly Sales",
    "start_cell": "A1",
    "end_cell": "E5"
  }
}
```

### 5. فحص هيكل دفتر العمل
```json
{
  "tool": "get_workbook_info",
  "parameters": {
    "filepath": "reports/monthly-report.xlsx"
  }
}
```

## ممارسات جيدة

1. **مسارات الملف**: استخدم المسارات النسبية لسهولة النقل
2. **أسماء الأوراق**: استخدم أسماء وصفية للأوراق
3. **هيكل البيانات**: نظم البيانات بعناوين واضحة
4. **قراءة النطاق**: حدد النطاقات لمجموعات البيانات الكبيرة
5. **معالجة الأخطاء**: تحقق من وجود الملف قبل العمليات

## الأنماط الشائعة

### نمط استيراد البيانات
1. إنشاء دفتر عمل
2. كتابة البيانات الخام
3. القراءة للتحقق من الصحة
4. المعالجة باستخدام الصيغ

### تقارير متعددة الأوراق
1. إنشاء دفتر عمل مع ورقة رئيسية
2. إضافة أوراق ملخص/تحليل
3. كتابة البيانات في كل ورقة
4. ربط الأوراق باستخدام الصيغ

### التحقق من البيانات
1. كتابة البيانات
2. القراءة للتحقق من مدى محدد
3. التحقق من سلامة البيانات
4. معالجة القيم المفقودة 
{{< app/cells/assistant language="nodejs-cpp" >}}
