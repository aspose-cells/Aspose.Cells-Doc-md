---
title: Как использовать Aspose.Cells для Python via Java в среде Gunicorn+Flask
type: docs
weight: 40
url: /ru/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: В этом разделе сравниваются компоненты Aspose.Cells для Python via Java и некоторые другие библиотеки операций Excel Python.
keywords: Python Excel, Excel Python, Excel Python via Java, Python via Java Excel, Почему Aspose.Cells для Python via Java, Почему не xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

Этот учебный материал показывает, как разработчики могут создать простое приложение (Hello World) с помощью Aspose.Cells для Python via Java. Приложение создает файл Microsoft Excel со словами Hello World в указанной ячейке листа.

{{% /alert %}}



## **Полная подготовка окружения**

Окружение для запуска этого руководства — Ubuntu: 20.04, вы можете настроить его в соответствии со своей ситуацией. Чтобы гарантировать правильное выполнение примеров, необходимо установить некоторые необходимые инструменты. Ниже представлен краткий пошаговый гид, который поможет вам завершить этот процесс. Обратите внимание, что это лишь пример, конкретные детали могут отличаться в зависимости от вашей системы и потребностей.

### Python

Если не установлен, установите его следующим образом:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
Проверить версию
```
python3 --version
pip3 --version
```

### Java
Если не установлен, установите его следующим образом:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
Проверить версию
```
java -version
```

### виртуальная среда virtualenv
Виртуальная среда установлена в соответствии с вашими текущими потребностями. Рекомендуется использовать виртуальные среды для управления зависимостями проекта как в разработке, так и в производственной среде.
Пожалуйста, следуйте следующей команде для установки:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
Создать виртуальную среду
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
Запустить виртуальную среду
```
source myenv/bin/activate
```

***Внимание: если используется виртуальная среда, последующие операции требуют предварительной активации соответствующей виртуальной среды***

### Flask
Если не установлен, выполните следующую команду для установки:
```
pip install Flask
```

### Gunicorn
Если не установлен, выполните следующую команду для установки:
```
pip install gunicorn
```

### Jpype
Если не установлен, выполните следующую команду для установки:
```
pip install jpype1
```

### aspose-cells
Если не установлен, выполните следующую команду для установки:
```
pip install aspose-cells
```

## **Создание приложения Hello World**

Для создания приложения Hello World с использованием Aspose.Cells API:

1. Создайте экземпляр класса [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook).
1. Примените лицензию:
   1. Если вы приобрели лицензию, используйте ее в своем приложении, чтобы получить доступ ко всей функциональности Aspose.Cells
   1. Если вы используете оценочную версию компонента (если вы используете Aspose.Cells без лицензии), пропустите этот шаг.
1. Создайте новый файл Microsoft Excel или откройте существующий файл, в котором вы хотите добавить/обновить некоторый текст.
1. Получите доступ к любой ячейке рабочего листа в файле Microsoft Excel.
1. Вставьте слова **Привет, мир!** в ячейку для доступа.
1. Сгенерируйте модифицированный файл Microsoft Excel.

Приведенные ниже примеры демонстрируют вышеуказанные шаги.

### **Создание рабочей книги**

В следующем примере создается новая рабочая книга с нуля, записываются слова "Hello World!" в ячейку A1 на первом листе и сохраняется файл.

Допустим, у нас есть тестовый путь "/app". В этом тестовом пути мы выполнит следующие работы.

#### Файлы приложения Flask: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### Файл пользовательского класса запуска Gunicorn: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### Запуск службы

Проверьте, установлены ли все необходимые для службы пакеты, затем запустите службу.

Если вы используете виртуальную среду python3-venv, вам нужно создать виртуальную среду в тестовом пути, запустить её и затем установить все необходимые инструменты.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### Проверка результатов

1. Откройте браузер и перейдите по адресу http://127.0.0.1:5000/.

2. Введите имя файла, который хотите сохранить, в поле ввода.

3. Нажмите кнопку 'Генерировать', чтобы сохранить файл.

После этого вы получите файл Excel с именем, соответствующим содержимому, которое вы ввели в текущем тестовом пути. Предварительный просмотр выглядит следующим образом:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## Использование Docker

Или вы можете поместить вышеуказанные операции в контейнер Docker. Очень просто использовать Docker для сборки среды, используемой в примере. Просто поместите вышеуказанные операции в файл Dockerfile.

Вот файл Dockerfile для справки. В нем перечислены необходимые наборы инструментов, требуемые для сборки среды.

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

Этот файл в основном используется для обеспечения среды зависимостей для проектов на Python. Вы можете изменить версию в этом файле по мере необходимости.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### Основные файлы

Основная структура файлов следующая:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### Запуск контейнера

Вы можете запустить контейнер с помощью следующей команды
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
