---
title: Passwort von verschlüsselten Dateien verifizieren
type: docs
weight: 10
url: /de/java/verify-password-of-encrypted-excel-and-ods-files/
description: Verifizieren Sie das Passwort verschlüsselter Excel (xlsx, xlsb, xls, xlsm) und OpenOffice (ODS) Dateien mithilfe von Java Codes.
---

{{% alert color="primary" %}}
Wenn Excel (xlsx, xlsb, xls, xlsm) und OpenOffice (ODS)-Dateien mit einem Passwort geschützt sind, unterstützt Aspose.Cells for Java eine einfache Passwortprüfung, ohne bestimmte Daten der Dateien zu analysieren.
{{% /alert %}}

## **Das Passwort der verschlüsselten Datei verifizieren**

Um das Passwort der verschlüsselten Datei zu überprüfen, bietet Aspose.Cells for Java die Methode [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) an. Die Methode akzeptiert zwei Parameter, den Dateistream und das zu überprüfende Passwort.
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**VerifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#verifyPassword-java.io.InputStream-java.lang.String-) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.

### **Beispielcode:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-VerifyPassword-1.java" >}}

{{< app/cells/assistant language="java" >}}
