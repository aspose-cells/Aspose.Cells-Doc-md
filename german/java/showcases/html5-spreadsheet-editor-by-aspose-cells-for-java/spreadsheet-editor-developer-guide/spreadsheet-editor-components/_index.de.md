---
title: Tabellenkalkulations Editor  Komponenten
type: docs
weight: 50
url: /de/java/spreadsheet-editor-components/
---

**Inhaltsverzeichnis**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Arbeitsblattansicht](#SpreadsheetEditor-Components-WorksheetView)
- [Arbeitsmappen-Service](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

Der HTML5-Tabellenkalkulations-Editor besteht aus einigen Komponenten, die zusammenarbeiten, um das vollständige System zu bilden. Hier beschreiben wir Zweck und Rolle jeder Komponente.
### **Index.html**
Es handelt sich um eine JSF-Seite, die die Benutzeroberfläche des Editors und den Hauptendpunkt unserer Anwendung beschreibt. Alle Interaktionen zwischen Webbrowser und Server erfolgen über diesen Endpunkt.

Neben der Definition der Benutzeroberfläche werden alle Backend-Services hier mithilfe von JSF-Technologien angehängt. Wenn der Benutzer mit der Benutzeroberfläche interagiert, werden Ereignisse und Daten zwischen den Services und dem Benutzer hin- und hergesendet, um unsere Aufgaben, beispielsweise das Exportieren von Tabellenkalkulationen, abzuschließen.

Es hat zwei Hauptinteressensgebiete.

**Ribbon**

Der Registerkartenwerkzeugleistenbereich oben wird technisch als Ribbon bezeichnet. Er enthält Schaltflächen, Dropdowns, Optionsfelder, Radiomenüs, Textfelder und einige versteckte Felder, die zur Durchführung vieler Operationen in der Tabellenkalkulation verwendet werden. Diese Schaltflächen senden bei Klick Befehle an den Server und aktualisieren entsprechend das Blatt.

**Blatt**

Das Blatt besteht aus Zeilen und Spalten. Wenn Zellen angeklickt werden, wird das Ribbon entsprechend aktualisiert, ohne Anfragen an den Server zu senden, da alle Daten, die das Ribbon benötigt, an jede Zelle angehängt sind. Das Ribbon behält auch die ausgewählte Zelle, Zeile und Spalte im Auge, wenn der Benutzer durch das Blatt navigiert.

Jede Zelle hat ihren eigenen Inline-Editor, der sichtbar wird, wenn sich die Zelle im Bearbeitungsmodus befindet.
### **Arbeitsblattansicht**
Es handelt sich um ein viewbezogenes JSF-Backend-Bean, das dafür verantwortlich ist, die dynamischen Inhalte der Benutzeroberfläche zu verwalten, die in index.html beschrieben sind. Es enthält Ereignisbehandler für Ajax-Anfragen, die ausgelöst werden, wenn der Benutzer mit der Benutzeroberfläche interagiert.
### **Arbeitsmappen-Service**
Der WorkbookService ist ein viewbezogenes JSF-Backend-Bean. Es fungiert als Servicekomponente und lädt und entlädt die Tabellenkalkulation mithilfe anderer Dienste. Er hat die folgenden Endpunkte:

**init**

Der **init** ist eine **PostConstruct**-Methode, die unmittelbar nach Abschluss der Objekterstellung durch den Java Application Server ausgeführt wird. Er überprüft auf **url**-Parameter in der Anforderungsparameterkarte und lädt die entsprechende Tabelle aus dem angegebenen Speicherort, falls möglich.

**destroy**

Es ist dafür verantwortlich, alle erworbenen Ressourcen aufzuräumen, wenn sie nicht mehr benötigt werden.
### **LoaderService**
Es erstellt Instanzen von Tabellenkalkulationen und behält sie im Speicher, solange sie benötigt werden.
### **CellsService**
Der **CellsService** verwaltet den Cache von Zeilen, Spalten, Zellen, Formaten und der Struktur von Arbeitsblättern.
