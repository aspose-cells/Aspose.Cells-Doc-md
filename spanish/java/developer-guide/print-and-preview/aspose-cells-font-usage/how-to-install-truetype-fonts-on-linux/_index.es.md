---
title: Cómo instalar fuentes TrueType en Linux
type: docs
weight: 20
url: /es/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

El escenario más probable es que estés usando Aspose.Cells para convertir hojas de cálculo a PDF. Si estás haciendo esto en un sistema operativo que no es de Windows, como Linux, este tema explica cómo asegurarte de que Aspose.Cells renderice tus hojas de cálculo con la mejor fidelidad posible.

Para asegurarte de que las hojas de cálculo convertidas por Aspose.Cells se vean lo más cercanas posibles al original, es posible que necesites instalar las "fuentes de Windows" o "fuentes TrueType" en tu sistema Linux, ya que las fuentes TrueType más comúnmente usadas no vienen preinstaladas en las distribuciones de Linux de forma predeterminada.

Hay dos formas principales de obtener fuentes TrueType en un sistema Linux:

1. Copia archivos de fuentes (.TTF y .TTC) de una máquina con Windows a tu máquina Linux.
1. Instala un paquete de fuentes TrueType, como msttcorefonts.

{{% /alert %}}

## **Copia fuentes de una máquina con Windows**

Una forma fácil y rápida es copiar los archivos .TTF y .TTC del directorio C:\Windows\Fonts en una máquina con Windows a algún directorio en tu máquina con Linux. No es necesario instalar o registrar estas fuentes en Linux de ninguna manera, solo debes especificar la ubicación de las fuentes utilizando el método FontConfigs.setFontFolder en tu aplicación.

{{% alert color="primary" %}}

Según lo que podemos decir, Microsoft otorga licencias para que cualquiera pueda usar las fuentes libremente, pero verifica por ti mismo la licencia de la fuente.

{{% /alert %}}

## **Instalar un paquete de fuentes TrueType**

La información proporcionada a continuación te guiará paso a paso para instalar las fuentes TrueType más famosas de Microsoft en distribuciones de Linux como Fedora y Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Es posible que necesites privilegios a nivel 'root', por lo tanto, inicia sesión como 'root' o configura sudo.

{{% /alert %}}

Así es como se hace desde la Terminal.

1. Asegúrate de tener instalados los siguientes paquetes RPM.
   1. **rpm-build**: Si no está instalado, usa el siguiente comando para instalar el paquete rpm-build

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Si no está instalado, usa el siguiente comando

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. Descarga el archivo spec más reciente de msttcorefonts desde SourceForge usando el siguiente comando,

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Crea un archivo RPM usando el archivo spec previamente descargado y el siguiente comando,

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. El archivo RPM se almacenará en: /root/rpmbuild/RPMS/noarch/, instálalo como sigue,

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Reinicia la máquina para que los cambios surtan efecto.

Las instrucciones proporcionadas anteriormente instalarán el paquete Microsoft TTFs que incluye las siguientes familias de fuentes:

1. Andale Mono
1. Arial Black/Arial (Negrita, Cursiva, Negrita Cursiva)
1. Comic Sans MS (Negrita)
1. Courier New (Negrita, Cursiva, Negrita Cursiva)
1. Georgia (Negrita, Cursiva, Negrita Cursiva)
1. Impact
1. Tahoma
1. Times New Roman (Negrita, Cursiva, Negrita Cursiva)
1. Trebuchet (Negrita, Cursiva, Negrita Cursiva)
1. Verdana (Negrita, Cursiva, Negrita Cursiva)
1. Webdings

{{% alert color="primary" %}}

En Ubuntu, ve al Administrador de paquetes Synaptic. Encuentra e instala el paquete **ttf-mscorefonts-installer**.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
