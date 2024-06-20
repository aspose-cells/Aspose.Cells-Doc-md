---
title: Proteger o Quitar Protección al Libro de Trabajo Compartido
linktitle: Proteger o Desproteger el Libro Compartido
type: docs
weight: 70
url: /es/java/password-protect-or-unprotect-the-shared-workbook/
---

## **Escenarios de uso posibles**

Puede proteger o desproteger el libro compartido con Microsoft Excel, como se muestra en la siguiente captura de pantalla. Aspose.Cells también admite esta función con los métodos [**Workbook.protectSharedWorkbook()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#protectSharedWorkbook(java.lang.String)) y [**Workbook.unprotectSharedWorkbook()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotectSharedWorkbook(java.lang.String)).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **Proteger o Quitar Protección al Libro de Trabajo Compartido**

El siguiente código de muestra crea un libro y lo protege mientras permite el uso compartido, y lo guarda como [archivo de Excel de salida](55541800.xlsx). La captura de pantalla muestra que al intentar desprotegerlo, Microsoft Excel le pide que introduzca la contraseña para desprotegerlo.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PasswordProtectOrUnprotectSharedWorkbook.java" >}}
