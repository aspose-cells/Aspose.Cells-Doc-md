---
title: Преобразование Excel в ODS
type: docs
weight: 40
url: /ru/python-java/convert-excel-to-ods/
---
## **Преобразование Excel в ODS**
Файлы ODS создаются программой Calc, которая является частью Apache OpenOffice Suite. В файлах ODS хранятся данные, которые организованы в строки и столбцы и отформатированы с использованием стандарта OASIS OpenDocument на основе XML.

Aspose.Cells for Python via Java поддерживает рабочие файлы ODS. В следующих примерах показано преобразование Excel в файл ODS.
### **Прямое преобразование**
Самый простой способ преобразовать файл Excel в ODS — загрузить книгу и сохранить ее, передав[СохранитьФормат.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS) в качестве второго параметра[Книга.сохранить](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) метод.

В следующем фрагменте кода продемонстрировано преобразование Excel напрямую в ODS.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Сохраните документ ODS в спецификации ODF 1.1 или 1.2.**
Aspose.Cells for Python via Java поддерживает сохранение ODS файлов в спецификациях ODF 1.1 и ODF 1.2. Для этого API предоставляет[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) имущество. Установка этого свойства в**истинный** сохранит файл со спецификацией ODF 1.1. Значение по умолчанию[OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) является**ЛОЖЬ**, поэтому файл ODS, сохраненный без специальных настроек, сохраняется со спецификацией ODF 1.2.

В следующем фрагменте кода показано сохранение файлов ODS со спецификациями ODF 1.1 и 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
