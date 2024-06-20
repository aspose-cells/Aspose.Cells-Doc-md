---
title: Hücreleri Kırparak ve Yapıştırarak
type: docs
weight: 30
url: /tr/python-java/cut-and-paste-cells/
---

## **Hücreleri Kırp ve Yapıştır**
Aspose.Cells for Python via Java, hücreleri kırpıp yapıştırmak için yetenek sağlar. Bunun için API, [Cells](https://reference.aspose.com/cells/python/asposecells.api/Cells) koleksiyonunun [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) methodunu sağlar. [insertCutCells](https://reference.aspose.com/cells/python/asposecells.api/cells#insertCutCells\(com.aspose.cells.Range,%20int,%20int,%20int\)) metodu aşağıdaki parametreleri kabul eder.

- [Range](https://reference.aspose.com/cells/python/asposecells.api/Range): Kırpmak için hücre aralığı.
- Satır Dizini: Hücreleri eklemek için satırın dizini.
- Sütun Dizini: Hücreleri eklemek için sütunun dizini.
- [ShiftType](https://reference.aspose.com/cells/python/asposecells.api/ShiftType): Sütunların kaydırma yönü.

Aşağıdaki kod parçası, bir çalışma sayfası içinde hücreleri kırparak ve yapıştırarak nasıl kullanacağınızı gösterir.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-CutAndPasteCells.py" >}}
