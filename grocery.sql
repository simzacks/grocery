create table chains(
    chainid text primary key,
    chain text);

create table stores(
    storepk integer primary key,
    chainid text,
    subchainid text,
    storeid text,
    bikoretno text,
    storetype text,
    subchainname text,
    storename text,
    address text,
    city text,
    zipcode text,
    foreign key(chainid) references chains(chainid)
);

create table subchainitems(
    subchainitempk integer primary key,
    chainid text,
    subchainid text,
    itemcode text,
    itemtype text,
    manufacturername text,
    manufacturercountry text,
    manufactureitemdescription text,
    unitqty text,
    quantity text,
    bisweighted text,
    unitofmeasure text,
    qtyinpackage text,
    foreign key(chainid) references chains(chainid)
);


create table storeprices(
    storepricepk integer primary key,
    storepk integer,
    subchainitempk integer,
    itemprice numeric,
    unitofmeasureprice numeric,
    allowdiscount text,
    itemstatus text,
    priceupdatedate text,
    foreign key(storepk) references stores(storepk),
    foreign key(subchainitempk) references subchainitems(subchainitempk)
);

create table promotions(
    promotionpk integer primary key,
    storepk integer,
    promotionid text,
    allowmultiplediscounts text,
    promotiondescription text,
    promotionupdatedate date,
    promotionstartdate date
    promotionstarthour datetime,
    promotionenddate date,
    promotionendhour datetime,
    isweightedpromo text,
    minqty integer,
    rewardtype text,
    discountedprice numeric,
    minnoofitemofered int,
    additionalrestrictions text,
    clubs text,
    foreign key(storepk) references stores(storepk)
);

create table promotionitems(
    promotionitempk integer primary key,
    promotionpk integer,
    itemcode text,
    itemtype text,
    isgiftitem text,
    foreign key(promotionpk) references promotions(promotionpk)
);



insert into chains(chainid, chain) values('7290027600007', 'שופרשל');
