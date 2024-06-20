---
title: Aspose.Cells .NET for PHP
type: docs
weight: 40
url: /de/net/aspose-cells-net-for-php/
---

## **Erste Schritte**

### **Einführung**

### **Systemanforderungen und unterstützte Plattformen**

#### **Systemanforderungen**

**Folgende sind die Systemanforderungen zur Verwendung von Aspose.Cells .NET für PHP:**

- IIS mit installiertem PHP und PHP-Manager.
- Aspose.Total APIs.
- Aspose.Cells, die Interop-DLL- und TLB-Datei.

#### **Unterstützte Plattformen**

**Folgende Plattformen werden unterstützt:**

- PHP 5.3 oder höher
- Windows-Betriebssystem

### **Herunterladen und Konfigurieren**

#### **Erforderliche Bibliotheken herunterladen**

Die unten genannten erforderlichen Bibliotheken herunterladen. Diese sind erforderlich zur Ausführung von Beispielen zu Aspose.Cells Java für PHP.

- [Laden Sie Aspose.Cells for .NET (DLL oder MSI)-Dateien aus dem Download-Bereich herunter](https://downloads.aspose.com/cells/net)
- [Aspose.Cells for .NET Interop-DLL herunterladen](https://downloads.aspose.com/cells/net)

Wenn Sie die MSI-Version herunterladen, finden Sie Aspose.Cells.dll standardmäßig im Installationsort unter C:\Programme (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0-Ordner.
Falls Sie jedoch die DLL-Version heruntergeladen haben, können Sie diese extrahieren und dann Aspose.Cells.dll vom .NET 2.0-Ordner in Ihren „C:\Temp“-Ordner kopieren, um die Nutzung zu erleichtern.
Extrahieren Sie ebenfalls die Interop-Zip-Datei und kopieren Sie Aspose.Inteop.dll nach C:\Temp

#### **Beispiele von Social Coding Sites herunterladen**

Folgende Versionen von laufenden Beispielen können auf den unten genannten Social Coding Sites heruntergeladen werden:

-----

##### **GitHub**

- **Aspose.Cells .NET for PHP Examples**

  - [Aspose.Cells .NET for PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **Wie man den Quellcode auf der Windows-Plattform konfiguriert**

Bitte befolgen Sie diese einfachen Schritte, um den Quellcode zu öffnen und zu erweitern, während Sie verwenden:

##### **1. Registrieren Sie sowohl die dll- als auch die interop.dll-Dateien, z.B. Aspose.Cells.dll und Aspose.Cells.Interop.dll.**

{{< highlight java >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Aktivieren Sie COM- und DOTNET-Erweiterungen in PHP.**

Öffnen Sie in IIS den PHP-Manager und klicken Sie dann auf „Erweiterung aktivieren bzw. deaktivieren“. Suchen Sie nach php_com_dotnet.dll und stellen Sie sicher, dass es aktiviert ist.

##### **3. Konfigurieren Sie Aspose.Cells .NET für PHP Beispiele**

###### **Methode 1**

Klonen Sie die PHP-Beispiele von [github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
und führen Sie den folgenden Befehl aus

{{< highlight java >}}

 composer install

{{< /highlight >}}

###### **Methode 2**

Fügen Sie in die composer.json-Datei Ihres PHP-Projekts folgende Zeilen hinzu

{{< highlight java >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

und führen Sie den Installationsbefehl aus

{{< highlight java >}}

 composer install

{{< /highlight >}}

To read about composer visit <https://getcomposer.org/>

### **Unterstützung erweitern und beitragen**

#### **Unterstützung**

Von den allerersten Tagen von Aspose an wussten wir, dass es nicht ausreichen würde, unseren Kunden einfach gute Produkte anzubieten. Wir mussten auch guten Service liefern. Wir sind selbst Entwickler und verstehen, wie frustrierend es ist, wenn ein technisches Problem oder eine Eigenart der Software Sie daran hindert, das zu tun, was Sie tun müssen. Wir sind hier, um Probleme zu lösen, nicht sie zu schaffen.

Deshalb bieten wir kostenlosen Support an. Jeder, der unsere Produkte verwendet, egal ob sie sie gekauft haben oder eine Evaluierung durchführen, verdient unsere volle Aufmerksamkeit und Respekt.

Sie können alle Probleme oder Vorschläge im Zusammenhang mit Aspose.Cells .NET für PHP über eine der folgenden Plattformen melden:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Ausweiten und Beitrag leisten**

Aspose.Cells .NET für PHP ist Open Source und der Quellcode ist auf den unten aufgeführten großen sozialen Coding-Websites verfügbar. Entwickler werden ermutigt, den Quellcode herunterzuladen und durch das Vorschlagen oder Hinzufügen neuer Funktionen oder die Verbesserung der bestehenden dazu beizutragen, damit auch andere davon profitieren können.

#### **Quellcode**

Sie können den neuesten Quellcode von einem der folgenden Standorte erhalten

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Beispielscode-Beispiele**

Dieser Abschnitt umfasst die folgenden Themen

- [PHP-Programmierhandbuch](/cells/de/net/php-programmers-guide/)
  - [Arbeiten mit Dateien in PHP](/cells/de/net/working-with-files-in-php/)
    - [Dateiverwaltungs-Funktionen in PHP](/cells/de/net/file-handling-features-in-php/)
      - [Öffnen von Dateien in PHP](/cells/de/net/opening-files-in-php/)
      - [Speichern von Dateien in PHP](/cells/de/net/saving-files-in-php/)
    - [Dienstprogramm-Funktionen in PHP](/cells/de/net/utility-features-in-php/)
      - [Verschlüsselung von Dateien in PHP](/cells/de/net/encrypting-files-in-php/)
      - [Excel-zu-PDF-Konvertierung in PHP](/cells/de/net/excel-to-pdf-conversion-in-php/)
      - [Verwaltung von Dokumenteigenschaften in PHP](/cells/de/net/managing-document-properties-in-php/)
      - [Arbeitsblatt-zu-Bild-Konvertierung in PHP](/cells/de/net/worksheet-to-image-conversion-in-php/)
  - [Arbeiten mit Formeln in PHP](/cells/de/net/working-with-formulas-in-php/)
    - [Berechnen von Formeln in PHP](/cells/de/net/calculating-formulas-in-php/)
  - [Arbeiten mit Arbeitsblättern in PHP](/cells/de/net/working-with-worksheets-in-php/)
    - [Verwaltungsfunktionen in PHP](/cells/de/net/management-features-in-php/)
      - [Verwalten von Arbeitsblättern in PHP](/cells/de/net/managing-worksheets-in-php/)
        - [Arbeitsblätter zu vorhandener Excel-Datei in PHP hinzufügen](/cells/de/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Arbeitsblätter zu neuer Excel-Datei in PHP hinzufügen](/cells/de/net/add-worksheets-to-new-excel-file-in-php/)
        - [Entfernen von Arbeitsblättern unter Verwendung des Tabellenindex in PHP](/cells/de/net/removing-worksheets-using-sheet-index-in-php/)
        - [Entfernen von Arbeitsblättern unter Verwendung des Tabellennamens in PHP](/cells/de/net/removing-worksheets-using-sheet-name-in-php/)
