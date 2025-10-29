---
title: دمج أو إلغاء دمج نطاق الخلايا مع Golang عبر C++
linktitle: دمج أو إلغاء دمج مجموعة من الخلايا
type: docs
weight: 190
url: /ar/go-cpp/merge-or-unmerge-range-of-cells/
description: دمج وإلغاء دمج الخلايا في نطاق في Excel باستخدام كود Golang عبر C++.
keywords: دمج وإلغاء دمج الخلايا في نطاق باستخدام C++، دمج وإلغاء دمج الخلايا في النطاق باستخدام C++، دمج وإلغاء دمج الخلايا في النطاق مع C++، دمج وإلغاء دمج الخلايا في النطاق باستخدام C++، دمج وإلغاء دمج خلايا Excel باستخدام C++, دمج خلايا C++ في Excel، إلغاء دمج خلايا C++ في Excel، دمج خلايا في النطاق باستخدام C++
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لدمج أو تقسيم مجموعة من الخلايا. يوفر Aspose.Cells الأساليب [**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/) و [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/) لهذا الغرض. يشرح هذا المقال كيفية دمج مجموعة من الخلايا في خلية واحدة.

{{% /alert %}}

## **مثال**

يعرض الكود النموذجي التالي أولاً إنشاء نطاق - A1:D4 - ثم دمج الخلايا في النطاق إلى خلية واحدة باستخدام الطريقة [**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/). بالمثل، يمكنك تقسيم الخلايا عن طريق إنشاء نطاق واستدعاء الطريقة [**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeOrUnmergeRangeOfCells.go" >}}
