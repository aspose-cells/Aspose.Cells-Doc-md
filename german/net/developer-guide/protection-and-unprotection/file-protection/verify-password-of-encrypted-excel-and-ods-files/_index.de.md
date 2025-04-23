---
title: Passwort von verschlüsselten Dateien verifizieren
type: docs
weight: 10
url: /de/net/verify-password-of-encrypted-excel-and-ods-files/
description: Überprüfen Sie das Passwort von verschlüsselten Excel (xlsx, xlsb, xls, xlsm) und Open Office (ODS) Dateien mithilfe von CShape Codes.
---

{{% alert color="primary" %}}
Wenn Excel (xlsx, xlsb, xls, xlsm) und Open-Office (ODS) Dateien mit einem Passwort geschützt sind, unterstützt Aspose einfache Passwortüberprüfung ohne das Parsen bestimmter Daten der Dateien.
{{% /alert %}}

## **Das Passwort der verschlüsselten Datei verifizieren**

Um das Passwort der verschlüsselten Datei zu verifizieren, bietet Aspose.Cells for .NET die Methode [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword). Diese Methoden akzeptieren zwei Parameter: den Dateistream und das zu verifizierende Passwort.
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
