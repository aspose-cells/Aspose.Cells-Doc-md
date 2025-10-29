---
title: تحويل JSON إلى CSV باستخدام Golang عبر C++
linktitle: تحويل JSON إلى CSV
type: docs
weight: 210
url: /ar/go-cpp/convert-json-to-csv/
description: تعلم كيفية تحويل JSON إلى CSV باستخدام Aspose.Cells for C++ مع أمثلة JSON بسيطة ومتداخلة.
---

## **تحويل JSON إلى CSV**

يدعم Aspose.Cells تحويل JSON بسيط و JSON متداخل إلى CSV. لهذا، توفر API الفئات [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/). وتوفر الفئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) الخيارات لتنسيق JSON مثل [**SetIgnoreTitle**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/setignoretitle/) (يتجاهل العنوان إذا كانت المصفوفة خاصية لكائن) أو [**GetArrayAsTable()**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/getarrayastable/) (يعالج المصفوفة كجدول). وتعالج الفئة [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) JSON باستخدام الخيارات تنسيق التي تم تحديدها بواسطة فئة [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/).

يوضح الكود التالي استخدام فئتي [**JsonLayoutOptions**](https://reference.aspose.com/cells/go-cpp/jsonlayoutoptions/) و [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) لتحميل ملف JSON المصدر ([104398869.json]) وتوليد ملف CSV الإخراجي ([104398870.csv]).

### **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertJsonToCsv.go" >}}
