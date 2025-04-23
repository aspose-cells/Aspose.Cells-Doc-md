---
title: Passwort von verschlüsselten Dateien verifizieren
type: docs
weight: 10
url: /de/python-net/verify-password-of-encrypted-excel-and-ods-files/
description: Überprüfen Sie das Passwort von verschlüsselten Excel (xlsx, xlsb, xls, xlsm) und Open Office (ODS) Dateien mithilfe von CShape Codes.
---

{{% alert color="primary" %}}
Wenn Excel (xlsx, xlsb, xls, xlsm) und Open-Office (ODS) Dateien mit einem Passwort geschützt sind, unterstützt Aspose einfache Passwortüberprüfung ohne das Parsen bestimmter Daten der Dateien.
{{% /alert %}}

## **Das Passwort der verschlüsselten Datei verifizieren**

Um das Passwort der verschlüsselten Datei zu überprüfen, bietet Aspose.Cells für Python via .NET die [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password)-Methode. Diese Methoden akzeptieren zwei Parameter, den Dateistream und das zu überprüfende Passwort.
Der folgende Code-Schnipsel zeigt die Verwendung der Methode [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) zur Überprüfung, ob das angegebene Passwort gültig ist oder nicht.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}


