---
title: Aspose.Cells for Android via Java Instalación
type: docs
weight: 30
url: /es/java/aspose-cells-for-android-via-java-installation/
---

## **Requisitos del sistema**
Aspose.Cells para Android via Java es independiente de la plataforma y se puede utilizar en cualquier plataforma donde se haya instalado el entorno de ejecución de Android y funcionará en sistemas Android que ejecuten Android OS 2.0 o superior. En la actualidad, el componente ha sido probado con:

- Android 5.1 v 22
## **Instalar Aspose.Cells para Android via Java desde el Repositorio Maven**
1. Agregue el repositorio de maven en su archivo **build.gradle** 
1. Agregue el JAR 'Aspose.Cells para Android via Java' como una dependencia

{{< highlight java >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **Cómo usar Aspose.Cells para Android via Java**
Este tema lo guiará a través de los pasos necesarios para configurar Aspose.Cells para Android via Java en el entorno de desarrollo integrado (IDE) de Android Studio, asumiendo que ya tiene instalada la última versión de Android Studio en su máquina y también ha adquirido la última versión del paquete Aspose.Cells para Android via Java.

{{% alert color="primary" %}} 

Si aún no ha instalado Android Studio, primero debe adquirir la configuración de Android Studio e instalarla en su máquina. Puede descargar la última versión de Android Studio desde [aquí](https://developer.android.com/studio/index.html#win-bundle) mientras que los detalles sobre cómo instalar el IDE están disponibles [aquí](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

El paquete Aspose.Cells para Android via Java se puede descargar desde [aquí](https://downloads.aspose.com/cells/androidjava). Tenga en cuenta que cada paquete de lanzamiento de Aspose.Cells para Android via Java consta principalmente de 2 archivos como se detalla a continuación.

- **aspose-cells-x.x.x.jar** es el archivo de la biblioteca principal que contiene todos los espacios de nombres de la API de Aspose.Cells para Android via Java.
- **aspose-cells-x.x.x-libs.apk** es el APK que contiene el bcprov-jdk15-146.jar de terceros utilizado para las facilidades de encriptación y desencriptación ofrecidas por la API de Aspose.Cells para Android via Java.

{{% /alert %}} 
### **Comenzar con Aspose.Cells para Android via Java en Android Studio**
Una vez que se carga el IDE de Android Studio, haga clic en Archivo > Nuevo > Nuevo proyecto como se muestra a continuación.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

También puede crear un nuevo proyecto desde la pantalla de bienvenida de Android Studio como se muestra a continuación.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

A continuación, se le solicitará que especifique el nombre de la aplicación, el dominio y la ubicación para almacenar los archivos del proyecto. Puede optar por cambiar los valores predeterminados según su preferencia o dejarlos como están, y haga clic en Siguiente.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

En el siguiente paso, deberá especificar el dispositivo Android en el que desea alojar/ejecutar su aplicación. Una vez seleccionado, haga clic en el botón Siguiente.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

Ahora necesita seleccionar la Actividad de una lista predefinida de plantillas. Para mantener la demostración simple, hemos seleccionado la plantilla de Actividad Vacía como se muestra a continuación.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

Haga clic en el botón Finalizar en el cuadro de diálogo Personalizar la Actividad, ya que mantendremos todas las configuraciones predeterminadas tal como están.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

Tan pronto como haga clic en el botón Finalizar en el paso anterior, el IDE comenzará a crear el proyecto como se muestra a continuación. Deje que termine o haga clic en el botón Cancelar.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

Ahora el proyecto ha sido cargado en el IDE, sin embargo, es posible que desee cambiar la vista a Proyecto para poder ver la jerarquía completa de los archivos del proyecto. Para cambiar la vista, por favor verifique la siguiente captura de pantalla.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

Después de cambiar la vista a Proyecto, encuentre y cargue el archivo **build.gradle** en el editor y pegue el siguiente fragmento como se muestra a continuación.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

A continuación, agregaremos el archivo Jar de Aspose.Cells para Android via Java al proyecto. Hay 2 pasos importantes como se detalla a continuación.

- Copiar manualmente el archivo Jar de Aspose.Cells para Android via Java en la carpeta **\app\libs**.
- Agregar el archivo Jar de Aspose.Cells para Android via Java como Biblioteca al módulo como se muestra a continuación.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

Se le solicitará que seleccione el módulo al que desea agregar el archivo Jar de Aspose.Cells for Java.Android como biblioteca. Elija apropiadamente y haga clic en Aceptar.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

También es necesario agregar el archivo APK al proyecto. Debe copiar el APK a la carpeta **\app\src\main\assets**. Si no tiene la carpeta assets debajo de la carpeta principal, puede crear una haciendo clic derecho en el nodo principal en la vista del Proyecto. Seleccione Nuevo > Carpeta > Carpeta de activos.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

Una vez que se haya agregado el APK al proyecto, debe ser cargado por el proyecto. Hay 2 formas de cargar el APK como se detalla a continuación.

- Cargue el APK en una clase de aplicación personalizada utilizando el fragmento de código proporcionado a continuación y registre la clase de aplicación personalizada en el AndroidManifest.xml.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- Cargue el APK en el método OnCreate de MainActivity.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

Ahora estamos listos para escribir el código. Para mantener la demostración fácil de entender, hemos agregado un widget de Botón al diseño y vamos a manejar su evento de clic como se muestra a continuación.

{{< highlight java >}}

 private class TestTask extends AsyncTask<Void, String, Boolean> {

    @Override

    protected Boolean doInBackground(Void... params) {

        Boolean result = false;

        Workbook book = new Workbook();

        Worksheet sheet = book.getWorksheets().get(0);

        Cells cells = sheet.getCells();

        Cell cell = cells.get("A1");

        cell.putValue("Hello World!");

        try {

            book.save(SD_PATH + "output.xlsx");

        } catch (Exception e) {

            e.printStackTrace();

        }

        return result;

    }

}

{{< /highlight >}}

Cuando ejecute la aplicación utilizando el botón de reproducción en la interfaz del IDE (o usando Mayús + F10), el emulador cargará la aplicación como se muestra a continuación.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

Al hacer clic en el botón del emulador, se ejecutará el código para crear una nueva hoja de cálculo en la carpeta de almacenamiento externo del emulador. Puede acceder al archivo desde el Monitor de dispositivos Android como se muestra a continuación.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


