---
title: Warum keine Automatisierung
type: docs
weight: 20
url: /de/java/why-not-automation/
---

{{% alert color="primary" %}}

Warum sind Aspose-Komponenten eine weitaus bessere Option als die Microsoft Office-Automatisierung?*

Es gibt zwei Fragen, die wir bei Aspose am häufigsten hören:

1. **Müssen Ihre Produkte installiertes Microsoft Office erfordern, um ausgeführt zu werden?** 
   Die einfache Antwort lautet nein. Aspose-Komponenten sind völlig unabhängig und nicht mit der Microsoft Corporation verbunden, autorisiert, gesponsert oder anderweitig genehmigt.
1. **Warum sollten wir Aspose-Produkte verwenden anstatt Microsoft Office-Automatisierung zu nutzen?**
   Die kürzeste Antwort, die wir geben könnten, ist, dass es viele Gründe gibt, wobei der Hauptgrund darin besteht, dass Microsoft selbst dringend davon abrät, Office-Automatisierung von Softwarelösungen zu verwenden: [Überlegungen zur serverseitigen Automatisierung von Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Es gibt mehrere Gründe, warum Aspose-Komponenten eine bessere Alternative zur Automatisierung darstellen. Einige der wichtigsten Gründe sind:

- [Sicherheit](/cells/de/java/why-not-automation/#security)
- [Stabilität](/cells/de/java/why-not-automation/#security)
- [Skalierbarkeit/Geschwindigkeit](/cells/de/java/why-not-automation/#security)
- [Preis](/cells/de/java/why-not-automation/#security)
- [Funktionen](/cells/de/java/why-not-automation/#security)

Die wichtigsten Punkte werden unten beschrieben. Stellen Sie außerdem sicher, dass Sie die Links am Ende dieses Abschnitts besuchen.

{{% /alert %}}

## **Sicherheit**

Folgendes ist ein direktes Zitat aus dem oben genannten Microsoft-Artikel: *"Office-Anwendungen waren nie für die Verwendung serverseitig vorgesehen und berücksichtigen daher nicht die Sicherheitsprobleme, mit denen verteilte Komponenten konfrontiert sind. Das Office authentifiziert keine eingehenden Anforderungen und schützt Sie nicht davor, Makros unbeabsichtigt auszuführen oder einen anderen Server zu starten, der möglicherweise Makros von Ihrem serverseitigen Code ausführen kann. Öffnen Sie keine Dateien, die anonym von einem Web-Server hochgeladen wurden! Basierend auf den zuletzt festgelegten Sicherheitseinstellungen kann der Server Makros im Kontext eines Administrators oder Systems mit vollen Berechtigungen ausführen und Ihr Netzwerk gefährden! Außerdem verwendet das Office viele Client-side-Komponenten (wie Simple MAPI, WinInet und MSDAIPP), die Client-Authentifizierungsinformationen zwischenspeichern, um die Verarbeitung zu beschleunigen. Wenn das Office serverseitig automatisiert wird, kann eine Instanz mehr als einen Client bedienen, und da die Authentifizierungsinformationen für diese Sitzung zwischengespeichert wurden, ist es möglich, dass ein Client die zwischengespeicherten Anmeldeinformationen eines anderen Clients verwendet und dadurch nicht genehmigte Zugriffsberechtigungen durch die Imitation anderer Benutzer erhält."*

Aspose-Produkte sind sehr sicher. Aspose-Komponenten laufen im gleichen Benutzerkontext wie alle ASP.NET-Anwendungen, unter dem Benutzer ASPNET. Daher stellen Aspose-Komponenten keine potenzielle Gefahr für wichtige Systemressourcen dar. Darüber hinaus werden bei Öffnen eines Dokuments durch eine Aspose-Komponente Makros nicht automatisch ausgeführt. Aspose-Komponenten wurden mit dem Ziel entwickelt, Entwicklern zu ermöglichen, Office-Dateien zu erstellen, zu bearbeiten und zu speichern. Keines der Risiken, die mit dem Microsoft Office-Paket verbunden sind, ist in Aspose-Komponenten inhärent.

## **Stabilität**

Folgendes ist ein direktes Zitat aus dem oben genannten Microsoft-Artikel: *"Office 2000, Office XP und Office 2003 verwenden die Microsoft Windows Installer (MSI)-Technologie, um die Installation und die Selbstreparatur für einen Endbenutzer zu vereinfachen. MSI führt das Konzept "Bei erster Verwendung installieren" ein, was es ermöglicht, Funktionen dynamisch zur Laufzeit zu installieren oder zu konfigurieren (für das System oder häufiger für einen bestimmten Benutzer). In einer serverseitigen Umgebung verlangsamt dies sowohl die Leistung als auch die Wahrscheinlichkeit, dass ein Dialogfeld angezeigt wird, das den Benutzer auffordert, die Installation zu genehmigen oder eine entsprechende Installationsdiskette bereitzustellen. Obwohl es dazu gedacht ist, die Widerstandsfähigkeit des Office als Endbenutzerprodukt zu erhöhen, ist die Implementierung der MSI-Fähigkeiten des Office in einer serverseitigen Umgebung kontraproduktiv. Darüber hinaus kann die Stabilität des Office allgemein nicht gewährleistet werden, wenn es serverseitig ausgeführt wird, da es nicht für diese Art der Verwendung konzipiert oder getestet wurde. Die Verwendung des Office als Dienstkomponente auf einem Netzwerkserver kann die Stabilität dieses Computers und folglich Ihres gesamten Netzwerks beeinträchtigen. Wenn Sie planen, das Office serverseitig zu automatisieren, versuchen Sie, das Programm auf einen dedizierten Computer zu isolieren, der keine kritischen Funktionen beeinträchtigen kann und bei Bedarf neu gestartet werden kann."*

Da Aspose-Komponenten in eine einzige DLL verpackt sind, wird niemals Bedarf bestehen, zusätzliche Teile oder Stücke zu installieren, damit sie funktionieren. Aspose-Komponenten werden nur von .NET-Anwendungen verwendet und es gibt keinen Teil des Komponentencodes, der auf eine menschliche Antwort wartet. Aspose-Komponenten wurden gründlich getestet. Aspose-Komponenten werden von Unternehmen wie IBM, Hilton, Reader's Digest, Bank of America und vielen anderen verwendet.

## **Skalierbarkeit/Geschwindigkeit**

Folgendes ist ein direktes Zitat aus dem oben genannten Microsoft-Artikel: *"Serverseitige Komponenten müssen hoch reentrant, mehrfädige COM-Komponenten mit minimalem Overhead und hoher Durchsatz für mehrere Clients sein. Office-Anwendungen sind in fast jeder Hinsicht das genaue Gegenteil. Sie sind nicht-reentrant, STA-basierte Automatisierungsserver, die darauf ausgelegt sind, vielfältige, aber ressourcenintensive Funktionen für einen einzelnen Client bereitzustellen. Sie bieten wenig Skalierbarkeit als serverseitige Lösung und haben feste Grenzen für wichtige Elemente, wie z. B. Speicher, die in der Konfiguration nicht geändert werden können. Noch wichtiger ist, dass sie globale Ressourcen verwenden (wie speicherabbildende Dateien, globale Add-Ins oder Vorlagen und gemeinsam genutzte Automatisierungsserver), die die Anzahl der gleichzeitig ausführbaren Instanzen begrenzen können und zu Problemen bei Rennbedingungen führen können, wenn sie in einer Multi-Client-Umgebung konfiguriert sind. Entwickler, die planen, mehr als eine Instanz jeder Office-Anwendung gleichzeitig auszuführen, sollten in Betracht ziehen, den Zugriff auf die Office-Anwendung "zurückzuhalten" oder zu serialisieren, um mögliche Deadlocks oder Datenbeschädigungen zu vermeiden."*

Aspose-Komponenten sind hoch skalierbar und blitzschnell. Büroanwendungen wurden nicht für die gleichzeitige Verwendung durch Hunderte und Tausende von Benutzern konzipiert; Aspose-Komponenten sind jedoch genau dafür konzipiert. Unsere Komponenten sind eine echte .NET-Lösung und funktionieren einwandfrei, egal ob auf einem einzelnen Server, der eine einzelne Anwendung unterstützt, oder auf einem lastausgeglichenen Webfarm, die eine unternehmensweite Anwendung unterstützt.

## **Preis**

Wenn eine Anwendung die Microsoft Office-Automatisierung nutzt, muss für jeden Rechner, auf dem die Anwendung ausgeführt wird, eine Kopie von Microsoft Office erworben werden. Oft muss eine Anwendung möglicherweise eine Office-Datei erstellen oder bearbeiten, ohne dass der Benutzer Office benötigt. Aspose bietet eine sehr [kostengünstige](https://purchase.aspose.com/buy), Lizenz zur kostenlosen Weiterverteilung, die die Bereitstellung an eine unbegrenzte Anzahl von Benutzern ohne Lizenzprobleme ermöglicht.

Bei der Erstellung webbasierter Anwendungen ist es wichtig zu wissen, dass Microsoft Office-Automatisierungskomponenten weder für serverseitige Lösungen bepreist noch lizenziert sind; es gibt daher keine gute Lizenzierungslösung für die Bereitstellung von Webanwendungen, die die Microsoft Office-Komponenten nutzen. Aspose bietet eine sehr kostengünstige Lösung für serverbasierte Anwendungen.

## **Funktionen**

Aspose-Komponenten bieten alles, was für die Verwaltung von Office-Dateien erforderlich ist, und noch viel, viel mehr. Sie sind nach dem Grundsatz konzipiert, Entwicklern zu ermöglichen, die größten Ergebnisse mit dem geringsten Aufwand zu erzielen. Im Gegensatz zur Office-Automatisierung bieten die Aspose-Komponenten viele leistungsstarke, zeitsparende Funktionen. Zum Beispiel bietet [Aspose.Cells](https://products.aspose.com/cells/java/) Entwicklern die Möglichkeit, direkt aus einem **DataTable** oder einer **DataView** in eine Excel-Datei zu exportieren. Jede [Komponente](https://products.aspose.com/total/) in der Aspose-Familie bietet ihre eigenen einzigartigen, leistungsstarken Funktionen.

Der beste Teil beim Kauf einer Aspose-Komponente oder einer Komponentensuite ist der Zugriff auf unsere Entwicklungsteams. Unsere Entwicklungsteams erkennen, dass wenn Ihr Unternehmen eine Funktion benötigt, wahrscheinlich auch andere Unternehmen diese benötigen werden. Auch wenn nicht alle Funktionsanfragen hinzugefügt werden können, versuchen unsere Teams sehr aufgeschlossen und flexibel zu sein, wenn es um Unterstützung geht. Diese Einstellung hat dazu beigetragen, dass Aspose-Komponenten so leistungsstark geworden sind. Wenn Sie zusätzliche Funktionen von Office-Automatisierungsobjekten benötigen, sind die Chancen sehr gering, dass sie hinzugefügt werden.

## **Fazit**

{{% alert color="primary" %}}

In diesem Artikel wurden die Schlüsselpunkte erläutert, warum Aspose-Komponenten eine bessere Wahl als die Office-Automatisierung sind. Alle verschiedenen Aspose-Komponenten bieten eine risikofreie, unverbindliche [Evaluierungsversion](https://products.aspose.com/total/). Wir empfehlen Ihnen, von dieser Evaluierung Gebrauch zu machen, um besser zu sehen, was Aspose für Ihre Anwendungen leisten kann.

Für weitere Informationen siehe die folgenden Internetartikel:

- [Überlegungen für die serverseitige Automatisierung von Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
