---
title: Warum nicht Automatisierung
type: docs
weight: 20
url: /de/java/why-not-automation/
---
{{% alert color="primary" %}}

Warum sind Aspose-Komponenten eine viel bessere Option als Microsoft Office Automation?*

Zwei Fragen hören wir hier unter Aspose am häufigsten:

1. **Benötigen Ihre Produkte die Installation von Microsoft Office, damit sie ausgeführt werden können?** 
 Die einfache Antwort ist nein. Aspose-Komponenten sind völlig unabhängig und weder mit der Microsoft Corporation verbunden noch autorisiert, gesponsert oder anderweitig genehmigt.
1. **Warum sollten wir Aspose-Produkte anstelle von Microsoft-Büroautomatisierung verwenden?**
Die kürzeste Antwort, die wir geben könnten, ist, dass es viele Gründe gibt, wobei der Hauptgrund darin besteht, dass Microsoft selbst dringend von der Office-Automatisierung durch Softwarelösungen abrät:[Überlegungen zur serverseitigen Automatisierung von Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2).

Es gibt mehrere Gründe, warum Aspose-Komponenten eine bessere Alternative zur Automatisierung sind. Einige der wichtigsten Gründe sind:

- [Sicherheit](/cells/de/java/why-not-automation/#security)
- [Stabilität](/cells/de/java/why-not-automation/#security)
- [Skalierbarkeit/Geschwindigkeit](/cells/de/java/why-not-automation/#security)
- [Preis](/cells/de/java/why-not-automation/#security)
- [Merkmale](/cells/de/java/why-not-automation/#security)

Die wichtigsten Punkte sind unten beschrieben. Besuchen Sie auch unbedingt die Links am Ende dieses Abschnitts.

{{% /alert %}}

## **Sicherheit**

 Das Folgende ist ein direktes Zitat aus dem oben genannten Artikel Microsoft:*„Office-Anwendungen waren nie für den serverseitigen Einsatz gedacht und berücksichtigen daher nicht die Sicherheitsprobleme, mit denen verteilte Komponenten konfrontiert sind. Das Office authentifiziert keine eingehenden Anfragen und schützt Sie nicht vor dem unbeabsichtigten Ausführen von Makros oder dem Starten eines anderen Servers die Makros ausführen könnten, aus Ihrem serverseitigen Code. Öffnen Sie keine Dateien, die von einem anonymen Web auf den Server hochgeladen werden! Basierend auf den zuletzt festgelegten Sicherheitseinstellungen kann der Server Makros in einem Administrator- oder Systemkontext ausführen volle Rechte und gefährden Ihr Netzwerk!Außerdem verwendet Office viele Client-seitige Komponenten (wie Simple MAPI, WinInet und MSDAIPP), die Client-Authentifizierungsinformationen zwischenspeichern können, um die Verarbeitung zu beschleunigen.Wenn Office serverseitig automatisiert wird , kann eine Instanz mehr als einen Client bedienen, und da Authentifizierungsinformationen für diese Sitzung zwischengespeichert wurden, ist es möglich, dass ein Client den Cache verwenden kann d-Anmeldeinformationen eines anderen Clients und erhalten dadurch nicht gewährte Zugriffsberechtigungen, indem Sie sich als andere Benutzer ausgeben."*

Aspose Produkte sind sehr sicher. Aspose-Komponenten werden im selben Benutzerkontext wie alle ASP.NET-Anwendungen unter dem ASPNET-Benutzer ausgeführt. Daher stellen Aspose-Komponenten kein potenzielles Risiko für wichtige Systemressourcen dar. Außerdem werden Makros nicht automatisch ausgeführt, wenn ein Dokument von einer Aspose-Komponente geöffnet wird. Aspose-Komponenten wurden mit dem Ziel entwickelt, Entwicklern das Erstellen, Bearbeiten und Speichern von Office-Dateien zu ermöglichen. Keines der mit dem Office-Paket Microsoft verbundenen Risiken ist den Komponenten von Aspose eigen.

## **Stabilität**

 Das Folgende ist ein direktes Zitat aus dem oben genannten Artikel Microsoft:*„Office 2000, Office XP und Office 2003 verwenden die Microsoft Windows Installer (MSI)-Technologie, um die Installation und Selbstreparatur für Endbenutzer zu vereinfachen. MSI führt das Konzept der „Installation bei der ersten Verwendung“ ein, wodurch Funktionen dynamisch bereitgestellt werden können installiert oder zur Laufzeit konfiguriert (für das System oder häufiger für einen bestimmten Benutzer) In einer serverseitigen Umgebung verlangsamt dies sowohl die Leistung als auch die Wahrscheinlichkeit, dass ein Dialogfeld angezeigt wird, in dem der Benutzer aufgefordert wird, die Installation zu genehmigen oder stellen Sie einen geeigneten Installationsdatenträger bereit.Obwohl es darauf ausgelegt ist, die Widerstandsfähigkeit von Office als Endbenutzerprodukt zu erhöhen, ist die Implementierung von MSI-Funktionen durch Office in einer serverseitigen Umgebung kontraproduktiv.Darüber hinaus ist die Stabilität von Office im Allgemeinen , kann nicht garantiert werden, wenn die Serverseite ausgeführt wird, da es nicht für diese Art der Verwendung entwickelt oder getestet wurde. Die Verwendung von Office als Dienstkomponente auf einem Netzwerkserver kann die Stabilität dieses Computers beeinträchtigen und a Dies hat zur Folge, dass Ihr Netzwerk als Ganzes. Wenn Sie Office serverseitig automatisieren möchten, versuchen Sie, das Programm auf einem dedizierten Computer zu isolieren, der keine kritischen Funktionen beeinträchtigen kann und der bei Bedarf neu gestartet werden kann."*

Da Aspose-Komponenten in einer einzigen DLL gepackt sind, müssen keine zusätzlichen Teile oder Teile installiert werden, damit sie funktionieren. Aspose-Komponenten werden nur von .NET-Anwendungen verwendet, und es gibt keinen Teil des Komponentencodes, der darauf ausgelegt ist, auf eine menschliche Antwort zu warten. Aspose Komponenten wurden ausgiebig getestet. Aspose-Komponenten werden von Unternehmen wie IBM, Hilton, Reader's Digest, Bank of America und vielen mehr verwendet.

## **Skalierbarkeit/Geschwindigkeit**

 Das Folgende ist ein direktes Zitat aus dem oben genannten Artikel Microsoft:*„Serverseitige Komponenten müssen hochgradig ablaufinvariante Multithread-COM-Komponenten mit minimalem Overhead und hohem Durchsatz für mehrere Clients sein. Office-Anwendungen sind in fast jeder Hinsicht das genaue Gegenteil. Sie sind nicht ablaufinvariante, STA-basierte Automatisierungsserver, die es sind Sie sind darauf ausgelegt, vielfältige, aber ressourcenintensive Funktionalität für einen einzelnen Client bereitzustellen, bieten als serverseitige Lösung wenig Skalierbarkeit und haben feste Grenzen für wichtige Elemente wie Speicher, die nicht durch Konfiguration geändert werden können, und vor allem verwenden sie globale Ressourcen (z. B. speicherabgebildete Dateien, globale Add-Ins oder Vorlagen und gemeinsam genutzte Automatisierungsserver), die die Anzahl der Instanzen begrenzen können, die gleichzeitig ausgeführt werden können, und zu Wettlaufbedingungen führen können, wenn sie in einer Umgebung mit mehreren Clients konfiguriert sind planen, mehr als eine Instanz einer beliebigen Office-Anwendung gleichzeitig auszuführen, müssen das „Pooling“ oder die Serialisierung des Zugriffs auf die Office-Anwendung in Betracht ziehen, um potenzielle Todesfälle zu vermeiden Sperren oder Datenkorruption."*

Aspose-Komponenten sind hochgradig skalierbar und blitzschnell. Office-Anwendungen wurden nicht dafür entwickelt, von Hunderten und Tausenden von Benutzern gleichzeitig verwendet zu werden. Aspose-Komponenten sind jedoch genau dafür ausgelegt. Unsere Komponenten sind eine echte .NET-Lösung und funktionieren einwandfrei, egal ob auf einem einzelnen Server, der eine einzelne Anwendung betreibt, oder auf einer Webfarm mit Lastenausgleich, die eine unternehmensweite Anwendung betreibt.

## **Preis**

 Wenn eine Anwendung Microsoft Office-Automatisierung verwendet, muss eine Kopie von Microsoft Office für jeden Computer erworben werden, auf dem die Anwendung ausgeführt wird. Es kommt oft vor, dass eine Anwendung eine Office-Datei erstellen oder bearbeiten muss, der Benutzer jedoch nicht über Office verfügen muss. Aspose bietet ein sehr[kosteneffizient](https://purchase.aspose.com/buy), gebührenfreie Weiterverteilungslizenz, die eine Bereitstellung für eine unbegrenzte Anzahl von Benutzern ohne Lizenzsorgen ermöglicht.

Beim Erstellen webbasierter Anwendungen ist es wichtig zu wissen, dass Microsoft Office-Automatisierungskomponenten für serverseitige Lösungen weder preislich noch lizenziert sind; Daher gibt es keine gute Lizenzierungslösung für die Bereitstellung von Webanwendungen, die die Microsoft Office-Komponenten verwenden. Aspose bietet auch für serverbasierte Anwendungen eine sehr kostengünstige Lösung.

## **Merkmale**

 Aspose-Komponenten bieten alles, was zum Verwalten von Office-Dateien benötigt wird, und vieles mehr. Sie wurden mit der Philosophie entwickelt, Entwicklern zu ermöglichen, mit dem geringsten Arbeitsaufwand die besten Ergebnisse zu erzielen. Im Gegensatz zur Büroautomatisierung bieten Aspose-Komponenten viele leistungsstarke, zeitsparende Funktionen. Zum Beispiel,[Aspose.Cells](https://products.aspose.com/cells/java/) bietet Entwicklern die Möglichkeit, aus einer**Datentabelle** oder**Datenansicht** direkt in eine Excel-Datei.[Jede Komponente](https://products.aspose.com/total/) in der Aspose-Familie bietet seinen eigenen Satz einzigartiger, leistungsstarker Funktionen.

Das Beste am Kauf einer Aspose-Komponente oder einer Komponentensuite ist der Zugang zu unseren Entwicklungsteams. Unsere Entwicklungsteams wissen, dass, wenn es eine Funktion gibt, die Ihr Unternehmen benötigt, höchstwahrscheinlich auch andere Unternehmen diese benötigen werden. Obwohl nicht jede Funktionsanfrage hinzugefügt werden kann, versuchen unsere Teams, bei der Bereitstellung von Unterstützung sehr aufgeschlossen und flexibel zu sein. Diese Denkweise hat Aspose-Komponenten geholfen, so leistungsfähig zu werden, wie sie sind. Wenn Sie zusätzliche Funktionen von Office-Automatisierungsobjekten benötigen, sind Ihre Chancen, dass sie hinzugefügt werden, sehr, sehr gering.

## **Fazit**

{{% alert color="primary" %}}

 Dieser Artikel hat die wichtigsten Punkte behandelt, warum Aspose-Komponenten eine bessere Wahl sind als die Office-Automatisierung. Alle verschiedenen Aspose-Komponenten bieten eine risikofreie und unverbindliche Nutzung[Testversion](https://products.aspose.com/total/). Wir empfehlen Ihnen, diese Bewertung zu nutzen, um besser zu sehen, was Aspose für Ihre Bewerbungen tun kann.

Weitere Informationen finden Sie in folgenden Internetartikeln:

- [Überlegungen zur serverseitigen Automatisierung von Office](https://support.microsoft.com/en-us/topic/considerations-for-server-side-automation-of-office-48bcfe93-8a89-47f1-0bce-017433ad79e2)

{{% /alert %}}
