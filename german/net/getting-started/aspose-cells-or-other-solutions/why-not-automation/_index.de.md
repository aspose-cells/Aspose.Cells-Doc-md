---
title: Warum keine Automatisierung
type: docs
weight: 50
url: /de/net/why-not-automation/
---

{{% alert color="primary" %}}

Warum sind Aspose-Komponenten eine weitaus bessere Option als die Microsoft Office-Automatisierung?*

{{% /alert %}}

## **Einführung**

Es gibt zwei Fragen, die wir bei Aspose am häufigsten hören:

1. **Müssen Ihre Produkte installiertes Microsoft Office erfordern, um ausgeführt zu werden?**
   Die einfache Antwort lautet nein. Aspose-Komponenten sind völlig unabhängig und nicht mit der Microsoft Corporation verbunden, autorisiert, gesponsert oder anderweitig genehmigt.
1. **Warum sollten wir Aspose-Produkte verwenden anstatt Microsoft Office-Automatisierung zu nutzen?**
   Die kürzeste Antwort, die wir geben könnten, ist, dass es viele Gründe gibt, wobei der Hauptgrund darin besteht, dass Microsoft selbst dringend davon abrät, Office-Automatisierung von Softwarelösungen zu verwenden: [Überlegungen zur serverseitigen Automatisierung von Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Es gibt mehrere Gründe, warum Aspose-Komponenten eine bessere Alternative zur Automatisierung darstellen. Einige der wichtigsten Gründe sind:

- Sicherheit
- Stabilität
- Skalierbarkeit/Geschwindigkeit
- Preis
- Funktionen

Die wichtigsten Punkte werden unten beschrieben. Stellen Sie außerdem sicher, dass Sie die Links am Ende dieses Abschnitts besuchen.

### **Sicherheit**

Nachfolgend ein direktes Zitat aus dem oben genannten Microsoft-Artikel:

*"Office-Anwendungen waren nie für die Verwendung serverseitig vorgesehen und berücksichtigen daher nicht die Sicherheitsprobleme, mit denen verteilte Komponenten konfrontiert sind. Office authentifiziert eingehende Anfragen nicht und schützt nicht vor unbeabsichtigtem Ausführen von Makros oder Starten eines anderen Servers, der Makros ausführen könnte, aus Ihrem serverseitigen Code. Öffnen Sie keine Dateien, die von einer anonymen Webseite auf den Server hochgeladen wurden! Basierend auf den zuletzt festgelegten Sicherheitseinstellungen kann der Server Makros unter einem Administrator- oder Systemkontext mit vollen Rechten ausführen und Ihr Netzwerk gefährden! Darüber hinaus verwendet Office viele clientseitige Komponenten (wie Simple MAPI, WinInet und MSDAIPP), die Client-Authentifizierungsinformationen zwischenspeichern können, um die Verarbeitung zu beschleunigen. Wenn Office serverseitig automatisiert wird, kann eine Instanz mehr als einen Client bedienen, und da Authentifizierungsinformationen für diese Sitzung zwischengespeichert wurden, kann es sein, dass ein Client die zwischengespeicherten Anmeldedaten eines anderen Clients verwenden kann und so nicht gewährte Zugriffsberechtigungen durch die Nachahmung anderer Benutzer erlangt."*

Aspose-Produkte sind sehr sicher. Aspose-Komponenten laufen im gleichen Benutzerkontext wie alle ASP.NET-Anwendungen, unter dem Benutzer ASPNET. Daher stellen Aspose-Komponenten keine potenzielle Gefahr für wichtige Systemressourcen dar. Darüber hinaus werden bei Öffnen eines Dokuments durch eine Aspose-Komponente Makros nicht automatisch ausgeführt. Aspose-Komponenten wurden mit dem Ziel entwickelt, Entwicklern zu ermöglichen, Office-Dateien zu erstellen, zu bearbeiten und zu speichern. Keines der Risiken, die mit dem Microsoft Office-Paket verbunden sind, ist in Aspose-Komponenten inhärent.

### **Stabilität**

Nachfolgend ein direktes Zitat aus dem oben genannten Microsoft-Artikel:

*"Office 2000, Office XP und Office 2003 verwenden die Microsoft Windows Installer (MSI)-Technologie, um die Installation und Selbstreparatur für den Endbenutzer zu erleichtern. MSI führt das Konzept der "Installation bei erstmaliger Verwendung" ein, das es ermöglicht, Funktionen zur Laufzeit (für das System oder häufiger für einen bestimmten Benutzer) dynamisch zu installieren oder zu konfigurieren. In einer serverseitigen Umgebung verlangsamt dies die Leistung und erhöht die Wahrscheinlichkeit, dass ein Dialogfeld erscheint, das den Benutzer zur Genehmigung der Installation auffordert oder eine geeignete Installationsdiskette bereitzustellen. Obwohl es dazu bestimmt ist, die Widerstandsfähigkeit des Office als Endbenutzerprodukt zu erhöhen, ist die Umsetzung der MSI-Fähigkeiten des Office in einer serverseitigen Umgebung kontraproduktiv. Darüber hinaus kann die Stabilität des Office im Allgemeinen nicht gewährleistet werden, wenn es serverseitig ausgeführt wird, da es nicht für diese Art der Verwendung entworfen oder getestet wurde. Die Verwendung von Office als Dienstkomponente auf einem Netzwerkserver kann die Stabilität dieses Computers und folglich Ihres gesamten Netzwerks beeinträchtigen. Wenn Sie planen, Office serverseitig zu automatisieren, versuchen Sie, das Programm auf einem dedizierten Computer zu isolieren, das keine kritischen Funktionen beeinträchtigen kann und bei Bedarf neu gestartet werden kann."*

Da Aspose-Komponenten in eine einzige DLL verpackt sind, wird niemals Bedarf bestehen, zusätzliche Teile oder Stücke zu installieren, damit sie funktionieren. Aspose-Komponenten werden nur von .NET-Anwendungen verwendet und es gibt keinen Teil des Komponentencodes, der auf eine menschliche Antwort wartet. Aspose-Komponenten wurden gründlich getestet. Aspose-Komponenten werden von Unternehmen wie IBM, Hilton, Reader's Digest, Bank of America und vielen anderen verwendet.

### **Skalierbarkeit/Geschwindigkeit**

Nachfolgend ein direktes Zitat aus dem oben genannten Microsoft-Artikel:

*"Serverseitige Komponenten müssen hoch reentrant, multithreaded COM-Komponenten mit minimalem Overhead und hoher Durchsatzrate für mehrere Clients sein. Office-Anwendungen sind in fast jeder Hinsicht das genaue Gegenteil. Sie sind nicht reentrant, STA-basierte Automatisierungsserver, die dazu entwickelt sind, vielfältige, aber ressourcenintensive Funktionalitäten für einen einzigen Client bereitzustellen. Sie bieten wenig Skalierbarkeit als serverseitige Lösung und haben feste Grenzen für wichtige Elemente wie Speicher, die nicht durch Konfiguration geändert werden können. Noch wichtiger ist, dass sie globale Ressourcen wie speichermapped Dateien, globale Add-Ins oder Vorlagen und gemeinsam genutzte Automatisierungsserver verwenden, die die Anzahl der gleichzeitig ausführbaren Instanzen begrenzen und zu Wettlaufbedingungen führen können, wenn sie in einer Multi-Client-Umgebung konfiguriert sind. Entwickler, die planen, mehr als eine Instanz einer Office-Anwendung gleichzeitig auszuführen, müssen das "Poolen" oder die Serialisierung des Zugriffs auf die Office-Anwendung in Betracht ziehen, um potenzielle Deadlocks oder Datenkorruption zu vermeiden."*

Aspose-Komponenten sind hoch skalierbar und blitzschnell. Büroanwendungen wurden nicht für die gleichzeitige Verwendung durch Hunderte und Tausende von Benutzern konzipiert; Aspose-Komponenten sind jedoch genau dafür konzipiert. Unsere Komponenten sind eine echte .NET-Lösung und funktionieren einwandfrei, egal ob auf einem einzelnen Server, der eine einzelne Anwendung unterstützt, oder auf einem lastausgeglichenen Webfarm, die eine unternehmensweite Anwendung unterstützt.

### **Preis**

Wenn eine Anwendung die Microsoft Office-Automatisierung nutzt, muss für jeden Rechner, auf dem die Anwendung ausgeführt wird, eine Kopie von Microsoft Office erworben werden. Oft muss eine Anwendung möglicherweise eine Office-Datei erstellen oder bearbeiten, ohne dass der Benutzer Office benötigt. Aspose bietet eine sehr [kostengünstige](https://purchase.aspose.com/buy), Lizenz zur kostenlosen Weiterverteilung, die die Bereitstellung an eine unbegrenzte Anzahl von Benutzern ohne Lizenzprobleme ermöglicht.

Bei der Erstellung webbasierter Anwendungen ist es wichtig zu wissen, dass die Microsoft Office-Automatisierungskomponenten nicht für serverseitige Lösungen preislich oder lizenzrechtlich festgelegt sind ([Lizenzierung der Office 2000-Webkomponenten und Office Server-Erweiterungen](#)); daher gibt es keine gute Lizenzlösung für die Bereitstellung von Webanwendungen, die die Microsoft Office-Komponenten nutzen. Aspose bietet auch für serverbasierte Anwendungen eine sehr preisgünstige Lösung.

### **Funktionen**

Aspose-Komponenten bieten alles, was für die Verwaltung von Office-Dateien erforderlich ist, und noch viel mehr. Sie sind so konzipiert, dass Entwickler die besten Ergebnisse mit minimalem Aufwand erzielen können. Im Gegensatz zur Office-Automatisierung bieten Aspose-Komponenten viele leistungsstarke, zeitsparende Funktionen. Beispielsweise bietet [Aspose.Cells](https://products.aspose.com/cells/) Entwicklern die Möglichkeit, direkt aus einem **DataTable** oder **DataView** in eine Excel-Datei zu exportieren. [Aspose.Words](https://products.aspose.com/words/) bietet eine ähnliche Funktion, die es Entwicklern ermöglicht, ein Word-Seriendokument direkt aus einem .NET-Datenobjekt zu erstellen. [Jede Komponente](https://products.aspose.com/total/) in der Aspose-Familie bietet ihre eigenen einzigartigen leistungsstarken Funktionen.

Der beste Teil beim Kauf einer Aspose-Komponente oder einer Komponentensuite ist der Zugriff auf unsere Entwicklungsteams. Unsere Entwicklungsteams erkennen, dass wenn Ihr Unternehmen eine Funktion benötigt, wahrscheinlich auch andere Unternehmen diese benötigen werden. Auch wenn nicht alle Funktionsanfragen hinzugefügt werden können, versuchen unsere Teams sehr aufgeschlossen und flexibel zu sein, wenn es um Unterstützung geht. Diese Einstellung hat dazu beigetragen, dass Aspose-Komponenten so leistungsstark geworden sind. Wenn Sie zusätzliche Funktionen von Office-Automatisierungsobjekten benötigen, sind die Chancen sehr gering, dass sie hinzugefügt werden.

## **Fazit**

{{% alert color="primary" %}}

In diesem Artikel wurden die wichtigsten Gründe behandelt, warum Aspose-Komponenten eine bessere Wahl als die Office-Automatisierung sind. Alle verschiedenen Aspose-Komponenten bieten eine risikofreie, unverbindliche [Auswertungsversion](https://downloads.aspose.com/total). Wir ermutigen Sie, von dieser Auswertung Gebrauch zu machen, um besser zu sehen, was Aspose für Ihre Anwendungen tun kann.


{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
