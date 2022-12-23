---
title: Cómo instalar fuentes TrueType en Linux
type: docs
weight: 20
url: /es/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

El escenario más probable es que esté usando Aspose.Cells para convertir hojas de cálculo a PDF. Si está haciendo esto en un sistema operativo no basado en Windows como Linux, este tema explica cómo asegurarse de que Aspose.Cells represente sus hojas de cálculo con la mejor fidelidad.

Para asegurarse de que las hojas de cálculo convertidas por Aspose.Cells se parezcan lo más posible al original, es posible que deba instalar "fuentes Windows" o "fuentes TrueType" en su sistema Linux porque las fuentes TrueType más utilizadas no vienen preinstaladas con Distribuciones de Linux por defecto.

Hay dos formas principales de obtener fuentes TrueType en un sistema Linux:

1. Copie archivos de fuentes (.TTF y .TTC) desde una máquina Windows a su máquina Linux.
1. Instale un paquete de fuentes TrueType, como msttcorefonts.

{{% /alert %}}

## **Copie fuentes de una máquina Windows**

Una manera fácil y rápida es copiar archivos .TTF y .TTC desde el directorio C:\Windows\Fonts en una máquina Windows a algún directorio en su máquina Linux. No necesita instalar o registrar estas fuentes en Linux de ninguna manera, solo necesita especificar la ubicación de las fuentes usando el método FontConfigs.setFontFolder en su aplicación.

{{% alert color="primary" %}}

Por lo que podemos decir, Microsoft licencia las fuentes para que cualquiera pueda usarlas libremente, pero verifique la licencia de la fuente usted mismo.

{{% /alert %}}

## **Instalar un paquete de fuentes TrueType**

La información proporcionada a continuación lo guiará paso a paso para instalar las fuentes TrueType más famosas de Microsoft en distribuciones de Linux como Fedora y Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Es posible que necesite privilegios de nivel 'root', por lo tanto, inicie sesión como 'root' o configure sudo.

{{% /alert %}}

He aquí cómo hacerlo usando la Terminal.

1. Asegúrese de tener instalados los siguientes paquetes RPM.
   1. **rpm-construir**: si no está instalado, use el siguiente comando para instalar el paquete rpm-build

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Si no está instalado, use el siguiente comando

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. Descargue el último archivo de especificaciones msttcorefonts de SourceForge usando el siguiente comando:

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Cree un archivo RPM utilizando el archivo de especificaciones descargado previamente y el siguiente comando,

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. El archivo RPM se almacenará en: /root/rpmbuild/RPMS/noarch/, instálelo de la siguiente manera,

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Reinicie la máquina para que los cambios surtan efecto.

Las instrucciones proporcionadas anteriormente instalarán el paquete Microsoft TTF, incluidas las siguientes familias de fuentes:

1. Andale Mono
1. Arial Black/Arial (Negrita, Cursiva, Negrita Cursiva)
1. Comic Sans MS (Negrita)
1. Courier New (negrita, cursiva, negrita cursiva)
1. Georgia (negrita, cursiva, negrita cursiva)
1. Impacto
1. Tahoma
1. Times New Roman (negrita, cursiva, negrita cursiva)
1. Trebuchet (negrita, cursiva, negrita cursiva)
1. Verdana (negrita, cursiva, negrita cursiva)
1. correas

{{% alert color="primary" %}}

 En Ubuntu, vaya al Administrador de paquetes Synaptic. Busque e instale el**ttf-mscorefonts-instalador** paquete.

{{% /alert %}}
