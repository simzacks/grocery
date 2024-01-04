create table chains(
    chainid text primary key,
    chain text);

create table stores(
    chainid text not null,
    subchainid text not null,
    storeid text not null,
    bikoretno text,
    storetype text,
    subchainname text,
    storename text,
    address text,
    city text,
    zipcode text,
    primary key(chainid, subchainid, storeid),
    foreign key(chainid) references chains(chainid)
);

create table storeitems(
    chainid text not null,
    subchainid text not null,
    storeid text not null,
    itemcode text not null,
    itemtype text,
    manufacturername text,
    manufacturercountry text,
    manufactureitemdescription text,
    unitqty text,
    quantity text,
    bisweighted text,
    unitofmeasure text,
    qtyinpackage text,
    itemprice numeric,
    unitofmeasureprice numeric,
    allowdiscount text,
    itemstatus text,
    priceupdatedate text,
    primary key (chainid, subchainid, storeid, itemcode),
    foreign key (chainid, subchainid, storeid) references stores(chainid, subchainid, storeid),
    foreign key(chainid) references chains(chainid)
);


create table promotions(
    chainid text not null,
    subchainid text not null,
    storeid text not null,
    promotionid text not null,
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
    primary key(chainid, subchainid, storeid, promotionid),
    foreign key(chainid, subchainid, storeid) references stores(chainid, subchainid, storeid)
);

create table promotionitems(
    chainid text not null,
    subchainid text not null,
    storeid text not null,
    promotionid text not null,
    itemcode text not null,
    itemtype text,
    isgiftitem text,
    primary key(chainid, subchainid, storeid, promotionid, itemcode),
    foreign key(chainid, subchainid, storeid, promotionid) references promotions(chainid, subchainid, storeid, promotionid)
);



insert into chains(chainid, chain) values('7290027600007', 'שופרשל');
