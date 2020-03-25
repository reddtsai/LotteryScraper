# Lottery Scraper

Sample Python reference scraping application, powered by Microsoft, based on GCP containers.

## Getting Started

### Requirement

- Python 3
    - pymysql
    - beautifulsoup4
- MySQL
    - table
        ``` sql
        CREATE TABLE `Lotto649` (
        `Term` int(11) NOT NULL COMMENT '期別',
        `No1` tinyint(4) NOT NULL COMMENT '奬號一',
        `No2` tinyint(4) NOT NULL COMMENT '奬號二',
        `No3` tinyint(4) NOT NULL COMMENT '奬號三',
        `No4` tinyint(4) NOT NULL COMMENT '奬號四',
        `No5` tinyint(4) NOT NULL COMMENT '奬號五',
        `No6` tinyint(4) NOT NULL COMMENT '奬號六',
        `NoS` tinyint(4) NOT NULL COMMENT '特別號',
        `Creater` varchar(50) NOT NULL,
        `CreateDate` datetime NOT NULL,
        PRIMARY KEY (`Term`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        ```

### Running

You can run scraper locally with makefile.

``` bash
make run
```

### Unit Testing

Test scraper module with makefile.

``` bash
make unittest
```

### Deployment

Deploy app to Google Compute Engine

``` bash
make deploy
```