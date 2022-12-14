---
title: Aspose.Cells .NET für PHP
type: docs
weight: 40
url: /de/net/aspose-cells-net-for-php/
---
## **Einstieg**

### **Einführung**

### **Systemanforderungen und unterstützte Plattformen**

#### **System Anforderungen**

**Im Folgenden sind die Systemanforderungen für die Verwendung von Aspose.Cells .NET für PHP aufgeführt:**

- IIS mit installiertem PHP und PHP Manager.
- Aspose.Total APIs.
- Aspose.Cells die Interop-DLL- und TLB-Datei.

#### **Unterstützte Plattformen**

**Im Folgenden sind die unterstützten Plattformen aufgeführt:**

- PHP 5.3 oder höher
- Windows OS

### **Herunterladen und konfigurieren**

#### **Erforderliche Bibliotheken herunterladen**

Laden Sie die unten aufgeführten erforderlichen Bibliotheken herunter. Diese sind für die Ausführung von Aspose.Cells Java für PHP-Beispiele erforderlich.

- [Laden Sie die Dateien Aspose.Cells for .NET (DLL oder MSI) aus dem Download-Bereich herunter](https://downloads.aspose.com/cells/net)
- [Laden Sie die Interop-DLL Aspose.Cells for .NET herunter](https://downloads.aspose.com/cells/net)

Wenn Sie die MSI-Version herunterladen, finden Sie Aspose.Cells.dll im installierten Verzeichnis, das standardmäßig der Ordner C:\Program Files (x86)\Aspose\Aspose.Cells for .NET\Bin\net2.0 ist.
Falls Sie jedoch die DLL-Version heruntergeladen haben, können Sie sie extrahieren und dann Aspose.Cells.dll aus dem Ordner .NET 2.0 in Ihren Ordner c:\temp kopieren, um die Verwendung zu vereinfachen.
Extrahieren Sie auf ähnliche Weise die Interop-Zip-Datei und kopieren Sie Aspose.Inteop.dll nach c:\temp

#### **Laden Sie Beispiele von Social-Coding-Sites herunter**

Die folgenden Versionen von Laufbeispielen stehen auf den unten genannten Social-Coding-Sites zum Download zur Verfügung:

-----

##### **GitHub**

- **Aspose.Cells .NET für PHP-Beispiele**

  - [Aspose.Cells .NET für PHP](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

#### **So konfigurieren Sie den Quellcode auf der Windows-Plattform**

Bitte befolgen Sie diese einfachen Schritte, um den Quellcode zu öffnen und zu erweitern, während Sie ihn verwenden:

##### **1. Registrieren Sie sowohl dll- als auch interop.dll-Dateien, z. B. Aspose.Cells.dll und Aspose.Cells.Interop.dll.**

{{< highlight "java" >}}

 Register both dll and interop.dll files e.g. Aspose.Cells.dll and Aspose.Cells.Interop.dll.

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.dll /codebase

Microsoft (R) .NET Framework Assembly Registration Utility 2.0.50727.7905

Copyright (C) Microsoft Corporation 1998-2004. All rights reserved.

Types registered successfully

C:\Windows\Microsoft.NET\Framework\v2.0.50727>regasm c:\cells\Aspose.Cells.Interop.dll /codebase

{{< /highlight >}}

##### **2. Aktivieren Sie COM- und DOTNET-Erweiterungen in PHP.**

Öffnen Sie in IIS den PHP-Manager und klicken Sie dann auf „Enable to Disable and Extension“. php finden_com_dotnet.dll und stellen Sie sicher, dass es aktiviert ist.

##### **3. Konfigurieren Sie Aspose.Cells .NET für PHP-Beispiele**

###### **Methode 1**

 Klonen Sie PHP-Beispiele von[github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)
und führen Sie den folgenden Befehl aus

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

###### **Methode 2**

Fügen Sie in der Datei composer.json Ihres PHP-Projekts die folgenden Zeilen hinzu

{{< highlight "java" >}}

 {

    "require": {

        "aspose-cells/Aspose.Cells-for-.NET_for_php": "dev-master"

    }

}

{{< /highlight >}}

und führen Sie den Installationsbefehl aus

{{< highlight "java" >}}

 composer install

{{< /highlight >}}

 Um über den Komponistenbesuch zu lesen<https://getcomposer.org/>

### **Erweitern und beitragen**

#### **Die Unterstützung**

Von den ersten Tagen der Aspose wussten wir, dass es nicht ausreichen würde, unseren Kunden nur gute Produkte zu geben. Wir mussten auch einen guten Service bieten. Wir sind selbst Entwickler und verstehen, wie frustrierend es ist, wenn ein technisches Problem oder eine Macke in der Software Sie daran hindert, das zu tun, was Sie tun müssen. Wir sind hier, um Probleme zu lösen, nicht um sie zu erschaffen.

Aus diesem Grund bieten wir kostenlosen Support an. Jeder, der unser Produkt verwendet, ob er es gekauft hat oder eine Bewertung verwendet, verdient unsere volle Aufmerksamkeit und unseren Respekt.

Sie können alle Probleme oder Vorschläge im Zusammenhang mit Aspose.Cells .NET für PHP über eine der folgenden Plattformen protokollieren:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/issues)

#### **Erweitern und beitragen**

Aspose.Cells .NET für PHP ist Open Source und sein Quellcode ist auf den unten aufgeführten wichtigen Social-Coding-Websites verfügbar. Entwickler werden ermutigt, den Quellcode herunterzuladen und einen Beitrag zu leisten, indem sie neue Funktionen vorschlagen oder hinzufügen oder die vorhandenen verbessern, damit auch andere davon profitieren können.

#### **Quellcode**

Den neuesten Quellcode erhalten Sie von einer der folgenden Stellen

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose_Cells_NET_for_PHP)

## **Beispielcodebeispiele**

Dieser Abschnitt enthält die folgenden Themen

- [Handbuch für PHP-Programmierer](/cells/de/net/php-programmers-guide/)
  - [Arbeiten mit Dateien in PHP](/cells/de/net/working-with-files-in-php/)
    - [Dateihandhabungsfunktionen in PHP](/cells/de/net/file-handling-features-in-php/)
      - [Öffnen von Dateien in PHP](/cells/de/net/opening-files-in-php/)
      - [Speichern von Dateien in PHP](/cells/de/net/saving-files-in-php/)
    - [Hilfsfunktionen in PHP](/cells/de/net/utility-features-in-php/)
      - [Verschlüsseln von Dateien in PHP](/cells/de/net/encrypting-files-in-php/)
      - [Konvertierung von Excel in PDF in PHP](/cells/de/net/excel-to-pdf-conversion-in-php/)
      - [Dokumenteigenschaften in PHP verwalten](/cells/de/net/managing-document-properties-in-php/)
      - [Umwandlung von Arbeitsblättern in Bilder in PHP](/cells/de/net/worksheet-to-image-conversion-in-php/)
  - [Arbeiten mit Formeln in PHP](/cells/de/net/working-with-formulas-in-php/)
    - [Berechnung von Formeln in PHP](/cells/de/net/calculating-formulas-in-php/)
  - [Arbeiten mit Arbeitsblättern in PHP](/cells/de/net/working-with-worksheets-in-php/)
    - [Verwaltungsfunktionen in PHP](/cells/de/net/management-features-in-php/)
      - [Arbeitsblätter in PHP verwalten](/cells/de/net/managing-worksheets-in-php/)
        - [Arbeitsblätter zu vorhandener Excel-Datei in PHP hinzufügen](/cells/de/net/add-worksheets-to-existing-excel-file-in-php/)
        - [Arbeitsblätter zu neuer Excel-Datei in PHP hinzufügen](/cells/de/net/add-worksheets-to-new-excel-file-in-php/)
        - [Entfernen von Arbeitsblättern mit dem Blattindex in PHP](/cells/de/net/removing-worksheets-using-sheet-index-in-php/)
        - [Entfernen von Arbeitsblättern unter Verwendung des Blattnamens in PHP](/cells/de/net/removing-worksheets-using-sheet-name-in-php/)
