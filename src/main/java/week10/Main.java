package week10;

import java.sql.Time;

import week10.decorator.CachedDocument;
import week10.decorator.MockedDocument;
import week10.decorator.TimeDocument;

public class Main {
    public static void main(String[] args) {
        MockedDocument mocked = new MockedDocument();
        TimeDocument timeDocument = new TimeDocument(mocked);
        System.out.println(timeDocument.parse());
        CachedDocument cachedDocument = new CachedDocument(mocked);
        System.out.println(cachedDocument.parse());
    }
}