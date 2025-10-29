---
title: как создать совместный редактор Excel с GridJs
type: docs
weight: 260
url: /ru/java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor/
keywords: GridJs,совместный,редактор Excel,таблица,Java
description: В этой статье рассказывается, как создать совместный редактор Excel с помощью Aspose.Cells.GridJs для Java.
aliases:
  - /java/aspose-cells-gridjs/collaborative-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-spreadsheet-editor/
  - /java/aspose-cells-gridjs/how-to-build-collaborative-excel-editor-using-gridjs/
---

# Руководство по совместному редактору Excel

## Обзор архитектуры

Следующая диаграмма показывает, как GridJs обеспечивает совместное редактирование несколькими пользователями, 
на базе Spring Boot, WebSocket-соединения и базы данных MySQL для управления состоянием.

![Архитектура совместного редактирования GridJs](gridjs_collaborative_architecture.png)

## Предварительные требования

Перед началом убедитесь, что у вас установлено следующее:

- **Java 8+**  
- **Maven**  
- **MySQL** (или другая поддерживаемая SQL-база данных)  
- (по желанию) **Docker**, если предпочитаете запускать в контейнерах  
- Действительная **лицензия Aspose.Cells** (или [временная лицензия](https://purchase.aspose.com/temporary-license))  

---

## Step 1: Clone the Demo Project

Clone the official [Aspose.Cells GridJs demo repository](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/master/Examples.GridJs.Collaborative):

```bash
git clone https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java.git
cd Aspose.Cells-for-Java/Examples.GridJs.Collaborative
```

---

## Step 2: Configure Collaborative Mode

Open the [`src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties) file and adjust the settings:

```properties
# Directory containing spreadsheet files
testconfig.ListDir=/app/wb

# Directory for storing cache files
testconfig.CachePath=/app/grid_cache

# Aspose.Cells license file
testconfig.AsposeLicensePath=/app/license

# Enable collaborative mode
gridjs.iscollabrative=true

# Database connection (example: MySQL)
spring.datasource.url=jdbc:mysql://localhost:3306/gridjsdemodb?createDatabaseIfNotExist=true&useUnicode=true&serverTimezone=UTC&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
spring.sql.init.platform=mysql
```

Это позволяет нескольким пользователям одновременно редактировать одну таблицу.  
Изменения сохраняются в базе данных и синхронизируются между клиентами в реальном времени.

---

## Step 3: Run the Application

Run with Maven:

```bash
mvn spring-boot:run
```

Или прямо из основного класса:

```
src/main/java/com/aspose/gridjsdemo/usermanagement/UserManagementApplication.java
```

---

## Step 4: Test Collaborative Editing

Open your browser and navigate to:  
👉 `http://localhost:8080/gridjsdemo/list`

Steps:

1. A login page appears. Click **Create User** to register User1 and log in. You will then see the file list.  
2. Open a file from the list. The spreadsheet editor will load.  
3. Copy the same URL into another browser window. It will redirect to the login page. Create User2 and log in.  
4. Both users now see the same spreadsheet.  
5. If User1 edits the spreadsheet, User2 will see the changes in real time.  
6. If User2 edits, User1 will see the changes as well.  
7. Users can also download and save the file.  

---

## Шаг 5: Запуск в Docker (необязательно)

Если вы запускаете в Docker, отредактируйте строку 10 файла [`docker-compose.yml`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/docker-compose.yml), чтобы сместить файл лицензии.  

Например, если ваш файл лицензии находится по пути `C:/license/aspose.lic`:

```yaml
volumes:
  - C:/license/aspose.lic:/app/license  # optional: set Aspose license file
```

Это отображает локальный файл в контейнере.

Затем выполните сборку и запуск:

```bash
docker-compose up --build
```

Доступ к приложению по адресу:  
👉 `http://localhost:8080/gridjsdemo/list`

---

## Key Configuration Details

### 1. Enable Collaborative Mode

In [`/src/main/resources/application.properties`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/application.properties):

```properties
gridjs.iscollabrative=true
```

В конфигурации на стороне сервера [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

```java
@Bean
public GridJsOptions gridJsOptions() {
    //..... other options
    //here we shall set true for collaborative mode
    options.setCollaborative(true);
    return options;
}
```

Или глобально:

```java
Config.setCollaborative(true);
```

В настройках загрузки на стороне клиента [`/src/main/resources/templates/file/index.html`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/resources/templates/file/index.html):

```js
const option = {
    //..... other options
    //here we shall set true for collaborative mode
    isCollaborative: true
    //..... other options
};
```

---

### 2. User System Integration

The demo uses **Spring Security** for a simple user system.  

You must provide a `CoWorkUserProvider` implementation to connect GridJs with your user system:

In server-side config [`/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/FileConfig.java):

For example: here we defined MyCustomUser to implement all the interfaces in CoWorkUserProvider.

```java
@Bean
public CoWorkUserProvider currentUserProvider() {
    return new MyCustomUser();
}
```


В [`/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/MyCustomUser.java):

```java
public class MyCustomUser implements CoWorkUserProvider {
    //Get the current login user name
    @Override
    public String getCurrentUserName() {
        return getCurrentUser().getUsername();
    }

    //Get the current login user Id
    @Override
    public Long getCurrentUserId() {
        return getCurrentUser().getUserId();
    }

    //Get the current login user permission
    @Override
    public CoWorkUserPermission getPermission() {
        return CoWorkUserPermission.EDITABLE;
    }

    private static CustomUserDetails getCurrentUser() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        if (authentication != null && authentication.getPrincipal() instanceof CustomUserDetails) {
            return (CustomUserDetails) authentication.getPrincipal();
        }
        throw new IllegalStateException("User not authenticated");
    }
}
```

---

### 3. WebSocket Configuration

The demo uses **Spring WebSocket** with STOMP.  

Example config:

In [`/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/messages/WebSocketConfig.java):

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic");
        config.setApplicationDestinationPrefixes("/app");
        config.setUserDestinationPrefix("/user");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

GridJs ожидает, что `messageTopic` совпадет с "/topic/opr", что является значением по умолчанию:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic/opr");
```

Или:

```java
@Bean
    public GridJsOptions gridJsOptions() {
	//.... other options
    	options.setMessageTopic("/topic/opr");
    	//.... other options
        return options;
    }
```

На стороне клиента:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws','/app/opr','/user/queue','/topic/opr');
```

Здесь, `/GridJs2/msg` соответствует маршруту, определенному в  
[`src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java`](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/master/Examples.GridJs.Collabrative/src/main/java/com/aspose/gridjsdemo/filemanagement/controller/GridJsOprController.java):

```java
@RequestMapping("/GridJs2/msg")
```

#### Пример с пользовательскими путями WebSocket

Если ваш сервер использует другую конфигурацию:

```java
public class WebSocketConfig implements WebSocketMessageBrokerConfigurer {
    @Override
    public void configureMessageBroker(MessageBrokerRegistry config) {
        config.enableSimpleBroker("/topic_gridjs");
        config.setApplicationDestinationPrefixes("/app_gridjs");
        config.setUserDestinationPrefix("/user_gridjs");
    }

    @Override
    public void registerStompEndpoints(StompEndpointRegistry registry) {
        registry.addEndpoint("/ws_gridjs")
                .setAllowedOrigins("http://localhost:8080")
                .withSockJS();
    }
}
```

Тогда вам нужно установить:

**Сторона сервера**:

```java
com.aspose.gridjs.Config.setMessageTopic("/topic_gridjs/opr");
```

или

```java
    @Bean
    public GridJsOptions gridJsOptions() {
	//.... other option
    	options.setMessageTopic("/topic_gridjs/opr");
    	//.... other option
        return options;
    }
```

**Клиентская сторона**:

```js
xs.setCollaborativeSetting('/GridJs2/msg','/ws_gridjs','/app_gridjs/opr','/user_gridjs/queue','/topic_gridjs/opr');
```

подробная документация по setCollaborativeSetting доступна [здесь](https://docs.aspose.com/cells/java/aspose-cells-gridjs/how-to-use-gridjs-client-api/)

> ⚠️ Примечание: по умолчанию демонстрационная конфигурация работает из коробки.  
Дополнительная настройка требуется только если ваше приложение настраивает WebSocket-ендпоинты.  

Также помните: режим совместной работы **не** поддерживает ленивую загрузку.  
Не включайте `Config.setLazyLoading(true)`.

---

## Additional Notes


- We can add **file uploads** to load and edit spreadsheet file from upload directory.  
- Integrate with **cloud storage** like AWS S3 or Azure Blob.  

---

## Заключение

С помощью Aspose.Cells.GridJs вы можете быстро создать мощный **совместный редактор Excel**.  
Комбинация Java backend, GridJs frontend, SQL хранилища и WebSocket сообщений обеспечивает надежное редактирование таблиц в реальном времени.

---

## Resources

- [Product Page](https://products.aspose.com/cells/java)  
- [Documentation](https://docs.aspose.com/cells/java/aspose-cells-gridjs/)  
- [API Reference](https://reference.aspose.com/cells/java/com.aspose.gridjs/)  
- [Support Forum](https://forum.aspose.com/c/cells)  
- [Free Online Apps](https://products.aspose.app/cells/family)  
