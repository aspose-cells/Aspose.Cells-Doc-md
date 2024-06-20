---
title: Преобразование Excel в ODS
type: docs
weight: 40
url: /ru/python-java/convert-excel-to-ods/
---

## **Преобразование Excel в ODS**
ODS-файлы создаются программой Calc, которая является частью пакета Apache OpenOffice. Файлы ODS хранят данные, организованные в строках и столбцах, и форматируются с использованием стандарта OASIS OpenDocument на основе XML.

Aspose.Cells для Python via Java поддерживает работу с файлами ODS. Ниже приведены примеры преобразования Excel в файл ODS.
### **Прямое преобразование**
Самый простой способ преобразовать файл Excel в ODS - загрузить книгу и сохранить ее, передав вторым параметром метода [Workbook.save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String,%20int\)) значение [SaveFormat.ODS](https://reference.aspose.com/cells/python/asposecells.api/saveformat#ODS).

Ниже приведен фрагмент кода, демонстрирующий прямое преобразование Excel в формат ODS

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToODSFiles.py" >}}
### **Ниже приведен фрагмент кода, демонстрирующий сохранение файлов ODS в спецификациях ODF 1.1 и 1.2.**
Aspose.Cells для Python via Java поддерживает сохранение файлов ODS в соответствии с спецификациями ODF 1.1 и ODF 1.2. Для этого API предоставляет свойство [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11). Установка этого свойства в **true** позволяет сохранить файл с спецификацией ODF 1.1. Значение по умолчанию [OdsSaveOptions.setStrictSchema11()](https://reference.aspose.com/cells/python/asposecells.api/odssaveoptions#IsStrictSchema11) равно **false**, поэтому ODS-файл, сохраненный без специальных настроек, сохраняется с спецификацией ODF 1.2.

Следующий фрагмент кода демонстрирует сохранение файлов ODS в соответствии с спецификациями ODF 1.1 и 1.2.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-SaveODSFilesWithSpecifications.py" >}}
