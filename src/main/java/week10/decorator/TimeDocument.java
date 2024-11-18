package week10.decorator;

import java.time.Duration;
import java.time.LocalTime;

import lombok.AllArgsConstructor;

@AllArgsConstructor
public class TimeDocument implements Document{
    private Document document;
    @Override
    public String parse(){
        LocalTime startTime = LocalTime.now();
        String parced = document.parse();
        LocalTime endTime = LocalTime.now();
        System.out.println("Time "+ Duration.between(startTime, endTime).getSeconds());
        return parced;
    }
    @Override
    public String getGcsPath() {
        return document.getGcsPath();
    }
}
