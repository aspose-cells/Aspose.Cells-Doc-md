---
title: Come installare i caratteri TrueType su Linux
type: docs
weight: 20
url: /it/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

Lo scenario più probabile è che tu stia utilizzando Aspose.Cells per convertire i fogli di calcolo in PDF. Se lo stai facendo su un sistema operativo non basato su Windows come Linux, questo argomento spiega come garantire che Aspose.Cells visualizzi i tuoi fogli di calcolo con la massima fedeltà.

Per assicurarti che i fogli di calcolo convertiti da Aspose.Cells appaiano il più vicino possibile all'originale, potresti dover installare "font Windows" o "font TrueType" sul tuo sistema Linux perché i font TrueType più comunemente usati non sono preinstallati con Distribuzioni Linux per impostazione predefinita.

Ci sono due modi principali per ottenere font TrueType su un sistema Linux:

1. Copia i file dei font (.TTF e .TTC) da una macchina Windows alla tua macchina Linux.
1. Installa un pacchetto di font TrueType, come msttcorefonts.

{{% /alert %}}

## **Copia i caratteri da una macchina Windows**

Un modo semplice e veloce è copiare i file .TTF e .TTC dalla directory C:\Windows\Fonts su una macchina Windows in una directory sulla tua macchina Linux. Non è necessario installare o registrare questi caratteri su Linux in alcun modo, è sufficiente specificare la posizione dei caratteri utilizzando il metodo FontConfigs.setFontFolder nell'applicazione.

{{% alert color="primary" %}}

Per quanto ne sappiamo, Microsoft concede in licenza i caratteri affinché chiunque possa utilizzarli liberamente, ma controlla tu stesso la licenza dei caratteri.

{{% /alert %}}

## **Installa un pacchetto di caratteri TrueType**

Le informazioni fornite di seguito ti guideranno passo dopo passo per installare i font TrueType più famosi di Microsoft su distribuzioni Linux come Fedora e Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Potresti aver bisogno di privilegi di livello 'root', quindi accedi come 'root' o configura sudo.

{{% /alert %}}

Ecco come farlo usando il Terminale.

1. Assicurati di aver installato i seguenti pacchetti RPM.
   1. **build-rpm**: Se non è installato, utilizzare il seguente comando per installare il pacchetto rpm-build

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Se non installato, utilizzare il seguente comando

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. Scarica l'ultimo file delle specifiche msttcorefonts da SourceForge usando il comando come segue,

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Costruisci un file RPM usando il file delle specifiche precedentemente scaricato e il seguente comando,

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Il file RPM verrà archiviato in: /root/rpmbuild/RPMS/noarch/, installalo come segue,

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Riavvia la macchina per rendere effettive le modifiche.

Le istruzioni fornite sopra installeranno il pacchetto Microsoft TTFs che include le seguenti famiglie di caratteri:

1. Andale Mono
1. Arial Black/Arial (grassetto, corsivo, grassetto corsivo)
1. Comic Sans MS (grassetto)
1. Courier New (grassetto, corsivo, grassetto corsivo)
1. Georgia (grassetto, corsivo, grassetto corsivo)
1. Impatto
1. Taoma
1. Times New Roman (grassetto, corsivo, grassetto corsivo)
1. Trabucco (grassetto, corsivo, grassetto corsivo)
1. Verdana (grassetto, corsivo, grassetto corsivo)
1. Intrecci

{{% alert color="primary" %}}

 Su Ubuntu, vai a Synaptic Package Manager. Trova e installa il file**programma di installazione di ttf-mscorefonts** pacchetto.

{{% /alert %}}
