---
title: Tabelleneditor - Komponenten
type: docs
weight: 50
url: /de/java/spreadsheet-editor-components/
---
**Inhaltsverzeichnis**

- [Index.html](#SpreadsheetEditor-Components-Index.html)
- [Arbeitsblattansicht](#SpreadsheetEditor-Components-WorksheetView)
- [WorkbookService](#SpreadsheetEditor-Components-WorkbookService)
- [LoaderService](#SpreadsheetEditor-Components-LoaderService)
- [CellsService](#SpreadsheetEditor-Components-CellsService)

Der HTML5-Tabellen-Editor besteht aus einigen wenigen Komponenten, die sich zu einem vollständigen System zusammenfügen. Hier beschreiben wir den Zweck und die Rolle jedes einzelnen.
### **Index.html**
Es ist eine JSF-Seite, die die Benutzeroberfläche des Editors und den Hauptendpunkt unserer Anwendung beschreibt. Alle Interaktionen zwischen Webbrowser und Server erfolgen über diesen Endpunkt.

Neben der Definition der Benutzeroberfläche werden hier alle Backend-Dienste mithilfe von JSF-Technologien angehängt. Wenn der Benutzer mit der Benutzeroberfläche interagiert, werden Ereignisse und Daten zwischen den Diensten und dem Benutzer hin und her geleitet, um unsere Aufgaben zu erledigen, z. B. das Exportieren von Tabellenkalkulationen.

Es hat zwei Hauptinteressengebiete.

**Schleife**

Der obere Bereich der Symbolleiste mit Registerkarten wird technisch als Multifunktionsleiste bezeichnet. Es enthält Schaltflächen, Dropdown-Menüs, Optionsmenüs, Textfelder und einige versteckte Felder, die verwendet werden, um viele Operationen in der Tabelle auszuführen. Wenn diese Schaltflächen angeklickt werden, senden sie Befehle an den Server und aktualisieren das Blatt entsprechend.

**Blatt**

Das Blatt besteht aus Zeilen und Spalten. Wenn auf Zellen geklickt wird, wird das Menüband entsprechend aktualisiert, ohne dass Anfragen an den Server gesendet werden, da alle vom Menüband benötigten Daten an jede Zelle angehängt werden. Die Multifunktionsleiste verfolgt auch die ausgewählte Zelle, Zeile und Spalte, wenn der Benutzer durch das Blatt navigiert.

Jede Zelle hat ihren eigenen Inline-Editor, der sichtbar wird, wenn sich eine Zelle im Bearbeitungsmodus befindet.
### **Arbeitsblattansicht**
Es ist eine ansichtsbezogene JSF-Backend-Bean, die für die Verwaltung der dynamischen Inhalte der in index.html beschriebenen Benutzeroberfläche verantwortlich ist. Es verfügt über Ereignishandler für Ajax-Anforderungen, die ausgelöst werden, wenn der Benutzer mit der Benutzeroberfläche interagiert.
### **WorkbookService**
Der WorkbookService ist eine JSF-Backend-Bean mit Ansichtsbereich. Es funktioniert als Dienstkomponente und lädt und entlädt die Tabelle mit Hilfe anderer Dienste. Es hat die folgenden Endpunkte:

**drin**

 Das**drin** ist**PostKonstrukt** Methode, die unmittelbar nach Abschluss der Objekterstellung durch den Java Application Server ausgeführt wird. Es prüfen**URL** -Parameter in der Anforderungsparameterzuordnung und lädt die entsprechende Tabelle von der angegebenen Stelle, falls möglich.

**zerstören**

Es ist dafür verantwortlich, alle erworbenen Ressourcen zu bereinigen, wenn sie nicht mehr benötigt werden.
### **LoaderService**
Es erstellt Instanzen von Tabellenkalkulationen und behält sie im Speicher, solange sie benötigt werden.
### **CellsService**
 Das**CellsService** verwaltet den Cache von Zeilen, Spalten, Zellen, Formatierung und Struktur von Arbeitsblättern.
