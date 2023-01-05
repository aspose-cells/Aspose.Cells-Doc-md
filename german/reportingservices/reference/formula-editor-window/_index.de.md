---
title: Formel-Editor-Fenster
type: docs
weight: 20
url: /de/reportingservices/formula-editor-window/
---
{{% alert color="primary" %}} 

Mit dem Formeleditor können Sie Formeln für einen Bericht erstellen.

{{% /alert %}} 

So bearbeiten Sie eine Formel in einer Microsoft-Excel-Zelle:

1. Wählen Sie in Microsoft Excel eine Zelle aus.
1.  Öffnen Sie den Dialog Formel bearbeiten durch Anklicken**Formel bearbeiten** auf der Werkzeugleiste.
   ([Hinzufügen von Reporting Services-Formeln](/cells/de/reportingservices/adding-reporting-services-formulas/) geht durch ein Beispiel, das eine Formel bearbeitet.)
 Der Dialog ist in Abschnitte unterteilt: den Bearbeitungsbereich oben und den Formelbereich unten. Verwenden Sie den Formelbereich, um den Bearbeitungsbereich zu füllen.
1.  Wählen Sie eine Kategorie (Benutzer, Parameter, Felder usw.) aus der aus**Berichtsfelder** Liste (die linke Liste).
1.  Wählen Sie den Typ aus**Funktionen** Liste (in der Mitte).
1.  Wählen Sie eine Option aus**Betreiber** Liste (die rechte Liste).
1.  Klicken**Einfügung**um den Ausdruck hinzuzufügen**Bearbeiten** Bereich.
1.  Klicken**Einfügung** wenn der Ausdruck vollständig ist.
 Die Formel wird in die Zelle eingefügt.

**Der Dialog Formel bearbeiten** 

![todo: Bild_alt_Text](formula-editor-window_1.png)

Das Dialogfeld „Formel bearbeiten“ ist in Abschnitte unterteilt, die unten beschrieben werden.
#### **Bereich bearbeiten**
 Dies ist der Bereich, in dem Sie eine Formel erstellen oder bearbeiten. Erstellen Sie eine Formel, indem Sie auf eine der in der aufgelisteten Komponenten doppelklicken**Berichtsfelder**, **Funktionen** oder**Betreiber** Listen. Wenn Sie eine Komponente auswählen, wird auch die erforderliche Syntax eingefügt. Sie können eine Formel auch manuell eingeben.
#### **Formelbereich**
Der Formelbereich enthält drei Abschnitte, von denen jeder Informationen auflistet, die zum Erstellen einer Formel verwendet werden.

- Berichtsfelder – die linke Liste listet alle Datenbankfelder auf, auf die der Bericht zugreifen kann. Es listet auch bereits erstellte Formeln oder Gruppen auf.
- Funktionen – die mittlere Liste enthält Funktionen, vorgefertigte Prozeduren, die Werte zurückgeben. Sie führen Berechnungen wie AVERAGE, SUM, COUNT, SIN, UPPERCASE und so weiter durch.
- Operatoren - die in Formeln verwendeten „Aktionsverben“. Operatoren beschreiben eine Operation oder Aktion, die zwischen zwei oder mehr Werten stattfinden soll. Beispiele für Operatoren: addieren, subtrahieren, kleiner als und größer als usw.
#### **Kontrollen**
Der Dialog hat mehrere Steuerelemente:

|**Schaltflächenname** |**Beschreibung** |
|:- |:- |
| Rückgängig machen| Macht eine Aktion rückgängig.|
| Paste| Fügt eine Zeichenfolge aus den im Formelbereich aufgelisteten Komponenten in den Bearbeitungsbereich ein.|
| Einfügung| Nimmt den Wert im Bearbeitungsbereich und fügt ihn als Formel in eine Zelle ein.|
| Ausgang| Schließt den Formeleditor.|
{{% alert color="primary" %}} 

Verwandte Themen:

- [Formelliste](/cells/de/reportingservices/formula-list/) - eine Liste von Feldern und Operatoren.

{{% /alert %}}
