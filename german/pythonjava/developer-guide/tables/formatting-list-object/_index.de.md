---
title: Listobjekt formatieren
type: docs
weight: 30
url: /de/python-java/formatting-list-object/
---

## **Listobjekt formatieren**
Eine Tabelle ist eine Reihe von Zeilen und Spalten, die verwandte Daten enthalten und unabhängig von den Daten in anderen Zeilen und Spalten verwaltet werden. Standardmäßig ist in der Tabelle in der Kopfzeile für jede Spalte eine Filterung aktiviert, damit Sie Ihre Listobjektdaten schnell filtern oder sortieren können. Sie können eine Gesamtzeile (eine spezielle Zeile in einer Liste, die eine Auswahl von Aggregatfunktionen bietet, die für die Arbeit mit numerischen Daten nützlich sind) zum Listobjekt hinzufügen, die eine Dropdown-Liste von Aggregatfunktionen für jede Zelle der Gesamtzeile bereitstellt.

Aspose.Cells unterstützt die Formatierung von Listobjekten. Hierfür bietet die API die Klassen [ListObject](https://reference.aspose.com/cells/python/asposecells.api/ListObject) und [TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType). Die Klasse [TableStyleType](https://reference.aspose.com/cells/python/asposecells.api/TableStyleType) enthält Konstanten, die die integrierten Tabellenstile repräsentieren. Der folgende Codeausschnitt erstellt ein neues Listobjekt und setzt den Tabellen-Stiltyp auf [TABLE_STYLE_MEDIUM_10](https://reference.aspose.com/cells/python/asposecells.api/tablestyletype#TABLE_STYLE_MEDIUM_10)



{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Tables-FormatListObject.py" >}}
