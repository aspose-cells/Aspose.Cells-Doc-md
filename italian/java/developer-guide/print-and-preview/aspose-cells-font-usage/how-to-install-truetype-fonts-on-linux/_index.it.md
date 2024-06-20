---
title: Come installare i font TrueType su Linux
type: docs
weight: 20
url: /it/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

Lo scenario più probabile è che stai utilizzando Aspose.Cells per convertire fogli di calcolo in PDF. Se stai facendo questo su un sistema operativo basato su Linux diverso da Windows, come Linux, questo argomento spiega come garantire che Aspose.Cells renderizzi i tuoi fogli di calcolo con la migliore fedeltà.

Per assicurarsi che i fogli di calcolo convertiti da Aspose.Cells appaiano il più possibile simili all'originale, potresti aver bisogno di installare "font Windows" o "font TrueType" sul tuo sistema Linux perché i font TrueType più comunemente utilizzati non sono preinstallati nelle distribuzioni Linux di default.

Ci sono due modi principali per ottenere i font TrueType su un sistema Linux:

1. Copia i file dei font (.TTF e .TTC) da una macchina Windows alla tua macchina Linux.
1. Installa un pacchetto di font TrueType, come msttcorefonts.

{{% /alert %}}

## **Copia i font da una macchina Windows**

Un modo facile e veloce è copiare i file .TTF e .TTC dalla directory C:\Windows\Fonts di una macchina Windows in una directory sulla tua macchina Linux. Non è necessario installare o registrare questi font su Linux in alcun modo, è sufficiente specificare la posizione dei font utilizzando il metodo FontConfigs.setFontFolder nella tua applicazione.

{{% alert color="primary" %}}

Per quanto possiamo dire, Microsoft concede in licenza i font affinché chiunque possa utilizzarli liberamente, ma ti preghiamo di verificare la licenza dei font per te stesso.

{{% /alert %}}

## **Installa un pacchetto di font TrueType**

Le informazioni fornite di seguito ti guideranno passo dopo passo per installare i font TrueType più famosi di Microsoft su distribuzioni Linux come Fedora e Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Potresti avere bisogno di privilegi di 'root', quindi accedi come 'root' o configura sudo.

{{% /alert %}}

Ecco come farlo utilizzando il Terminale.

1. Assicurati di avere installati i seguenti pacchetti RPM.
   1. **rpm-build**: Se non è installato, utilizza il seguente comando per installare il pacchetto rpm-build

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Se non è installato, utilizza il seguente comando

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. Scarica il file spec più recente di msttcorefonts da SourceForge utilizzando il comando come indicato,

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Costruisci un file RPM utilizzando il file spec scaricato in precedenza e il seguente comando,

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Il file RPM sarà memorizzato in: /root/rpmbuild/RPMS/noarch/, installalo come segue,

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Riavvia la macchina per rendere effettive le modifiche.

Le istruzioni fornire sopra installeranno il pacchetto Microsoft TTFs includendo le seguenti famiglie di caratteri:

1. Andale Mono
1. Arial Black/Arial (Grassetto, Corsivo, Grassetto Corsivo)
1. Comic Sans MS (Grassetto)
1. Courier New (Grassetto, Corsivo, Grassetto Corsivo)
1. Georgia (Grassetto, Corsivo, Grassetto Corsivo)
1. Impact
1. Tahoma
1. Times New Roman (Grassetto, Corsivo, Grassetto Corsivo)
1. Trebuchet (Grassetto, Corsivo, Grassetto Corsivo)
1. Verdana (Grassetto, Corsivo, Grassetto Corsivo)
1. Webdings

{{% alert color="primary" %}}

Su Ubuntu, vai al Gestore dei pacchetti Sinaptici. Trova e installa il pacchetto **ttf-mscorefonts-installer**.

{{% /alert %}}
